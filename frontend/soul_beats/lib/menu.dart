import 'package:flutter/material.dart';
import 'package:soul_beats/MyRoutes.dart';
import 'package:soul_beats/teluguold.dart';

class MenuApp1 extends StatefulWidget {
  const MenuApp1({Key key}) : super(key: key);

  @override
  _MenuApp1State createState() => _MenuApp1State();
}

class _MenuApp1State extends State<MenuApp1> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
          child: TeluguOld(urlForData: 'https://hhuu8.herokuapp.com/${MyVariables.menuName}',),
        ),
    );
  }
}
