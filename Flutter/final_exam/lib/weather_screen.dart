import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:dropdown_search/dropdown_search.dart';

import 'weather_model.dart';
import 'weather_service.dart';

class WeatherScreen extends StatefulWidget {
  @override
  _WeatherScreenState createState() => _WeatherScreenState();
}

class _WeatherScreenState extends State<WeatherScreen> {
  late Future<WeatherData> futureWeather;
  String? _selectedCity;
  static const String _apiKey = '00479a705e852aa4e1489f40d451c2c4';

  final Map<String, Map<String, double>> _cities = {
    'Berlin'    : {'lat': 52.52 , 'lon': 13.41 },
    'Bangkok'   : {'lat': 13.75 , 'lon': 100.50},
    'London'    : {'lat': 51.51 , 'lon': -0.13 },
    'New York'  : {'lat': 40.71 , 'lon': -74.01},
    'Tokyo'     : {'lat': 35.68 , 'lon': 139.76},
    'Paris'     : {'lat': 48.85 , 'lon': 2.35  },
    'Sydney'    : {'lat': -33.87, 'lon': 151.21},
    'Moscow'    : {'lat': 55.75 , 'lon': 37.62 },
    'Dubai'     : {'lat': 25.20 , 'lon': 55.27 },
    'Singapore' : {'lat': 1.35  , 'lon': 103.82},
    'Los Angeles': {'lat': 34.05, 'lon': -118.24},
    'Beijing'   : {'lat': 39.90 , 'lon': 116.40},
    'Seoul'     : {'lat': 37.57 , 'lon': 126.98},
    'Mumbai'    : {'lat': 19.08 , 'lon': 72.88 },
    'Cape Town' : {'lat': -33.92, 'lon': 18.42 },
  };

  @override
  void initState() {
    super.initState();
    _selectedCity = 'Berlin';
    futureWeather = _fetchWeatherFromCity(_selectedCity!);
  }

  Future<Map<String, double>> _getCoordinatesFromCity(String city) async {
    if (_cities.containsKey(city)) {
      return _cities[city]!;
    }

    final response = await http.get(Uri.parse(
      'http://api.openweathermap.org/geo/1.0/direct?q=$city&limit=1&appid=$_apiKey',
    ));

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      if (data.isNotEmpty) {
        return {
          'lat': data[0]['lat'].toDouble(),
          'lon': data[0]['lon'].toDouble(),
        };
      }
      throw Exception('City not found');
    } else {
      throw Exception('Failed to get coordinates');
    }
  }

  Future<WeatherData> _fetchWeatherFromCity(String city) async {
    try {
      final coords = await _getCoordinatesFromCity(city);
      final data = await WeatherService.fetchWeather(
          coords['lat']!, coords['lon']!);
      return WeatherData.fromJson(data);
    } catch (e) {
      rethrow;
    }
  }

  void _updateLocation() {
    if (_selectedCity != null) {
      setState(() {
        futureWeather = _fetchWeatherFromCity(_selectedCity!);
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueGrey[50],
      appBar: AppBar(
        title: const Text('Weather MUT'),
        backgroundColor: Colors.blue[700],
        elevation: 4,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            _buildCityDropdown(),
            const SizedBox(height: 20),
            FutureBuilder<WeatherData>(
              future: futureWeather,
              builder: (context, snapshot) {
                if (snapshot.hasData) {
                  final weather = snapshot.data!;
                  return Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      _buildCurrentWeather(weather.current),
                      const SizedBox(height: 20),
                      Text('Hourly Forecast',
                          style: TextStyle(
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                            color: Colors.white,
                          )),
                      const SizedBox(height: 10),
                      _buildHourlyList(weather.hourly),
                    ],
                  );
                } else if (snapshot.hasError) {
                  return Center(
                    child: Card(
                      color: Colors.red[100],
                      child: Padding(
                        padding: const EdgeInsets.all(16),
                        child: Text(
                          "Error: ${snapshot.error}",
                          style: TextStyle(color: Colors.red[900]),
                        ),
                      ),
                    ),
                  );
                }
                return const Center(
                  child: CircularProgressIndicator(
                    color: Colors.blue,
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCityDropdown() {
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            DropdownSearch<String>(
              popupProps: PopupProps.menu(
                showSearchBox: true,
                fit: FlexFit.loose,
                menuProps: MenuProps(
                  backgroundColor: Colors.white,
                  elevation: 4,
                ),
              ),
              items: _cities.keys.toList(),
              dropdownDecoratorProps: DropDownDecoratorProps(
                dropdownSearchDecoration: InputDecoration(
                  labelText: 'Select City',
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(8),
                  ),
                  filled: true,
                  fillColor: Colors.white,
                ),
              ),
              onChanged: (String? newValue) {
                setState(() {
                  _selectedCity = newValue;
                });
              },
              selectedItem: _selectedCity,
            ),
            const SizedBox(height: 10),
            ElevatedButton(
              onPressed: _updateLocation,
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue[700],
                foregroundColor: Colors.white,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(8),
                ),
                padding: const EdgeInsets.symmetric(vertical: 12),
                minimumSize: const Size(double.infinity, 0),
              ),
              child: const Text('Get Weather'),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCurrentWeather(CurrentData current) {
    final timeFormat = DateFormat('MMM d, y • HH:mm');
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Current Weather',
                style: TextStyle(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: Colors.blue[800],
                )),
            const SizedBox(height: 10),
            Text(
              timeFormat.format(DateTime.parse(current.time)),
              style: TextStyle(color: Colors.grey[600]),
            ),
            const SizedBox(height: 10),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  '${current.temperature.toStringAsFixed(1)}°C',
                  style: const TextStyle(
                    fontSize: 32,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.blue[100],
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(
                    'Wind: ${current.windSpeed.toStringAsFixed(1)} km/h',
                    style: TextStyle(color: Colors.blue[800]),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHourlyList(HourlyData hourly) {
    final timeFormat = DateFormat('HH:mm');
    return SizedBox(
      height: 160,
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        itemCount: hourly.time.length,
        itemBuilder: (context, index) {
          return Container(
            width: 100,
            margin: const EdgeInsets.only(right: 10),
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(12),
              boxShadow: [
                BoxShadow(
                  color: Colors.grey.withOpacity(0.2),
                  spreadRadius: 1,
                  blurRadius: 4,
                  offset: const Offset(0, 2),
                ),
              ],
            ),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  timeFormat.format(DateTime.parse(hourly.time[index])),
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
                Text(
                  '${hourly.temperatures[index].toStringAsFixed(1)}°C',
                  style: TextStyle(
                    fontSize: 18,
                    color: Colors.blue[700],
                  ),
                ),
                Text(
                  '${hourly.humidity[index]}%',
                  style: TextStyle(color: Colors.grey[600]),
                ),
                Text(
                  '${hourly.windSpeeds[index].toStringAsFixed(1)} km/h',
                  style: TextStyle(color: Colors.grey[600]),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}