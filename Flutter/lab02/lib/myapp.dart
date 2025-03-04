import 'package:flutter/material.dart';
import 'homescreen.dart';

class MyApp extends StatelessWidget {
  const MyApp({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Lab02'),
          leading: Icon(Icons.menu),
        ),
        body: HomeScreen(),
      ),
    );
  }
}
