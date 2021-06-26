import 'package:flutter/material.dart';
import 'package:animated_splash/animated_splash.dart';
import 'package:soul_beats/screen1.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return AnimatedSplash(
      imagePath: 'assets/soulbeatslogo.jpg',
      duration: 3500,
      home: Screen1(),
    );
  }
}
