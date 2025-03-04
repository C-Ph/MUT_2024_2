import 'package:flutter/material.dart';

class MyText extends StatelessWidget {

  final String text;

  const MyText(this.text, {
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Text(
      text,
      style: TextStyle(
        fontSize: 50,
        color: Colors.red,
        fontWeight: FontWeight.bold,
      ),
    );
  }
}
