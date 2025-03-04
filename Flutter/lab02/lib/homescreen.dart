import 'package:flutter/material.dart';
import 'package:lab02/mytext.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      color: Colors.yellow,
      child: const Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Icon(Icons.access_alarm),
          MyText('hello'),
          MyText('hgfhgf'),
        ],
      ),
    );
  }
}



