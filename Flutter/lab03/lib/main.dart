import 'package:flutter/material.dart';
import 'package:lab03/login_screen.dart';
import 'package:lab03/register_screen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: RegisterScreen(),
      ),
    );
  }
}
