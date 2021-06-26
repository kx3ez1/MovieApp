import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:soul_beats/DrawerCode.dart';
import 'package:soul_beats/MyRoutes.dart';
import 'package:soul_beats/teluguold.dart';

class Screen1 extends StatefulWidget {
  const Screen1({Key key}) : super(key: key);

  @override
  _Screen1State createState() => _Screen1State();
}

class _Screen1State extends State<Screen1> {
  @override
  Widget build(BuildContext context) {
    var selectedItem = 0;

    return Scaffold(
      body: TeluguOld(urlForData: MyVariables.teluguOld,),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: selectedItem,
        onTap: (value) {
          selectedItem = value;
          setState(() {});
           if(selectedItem !=0){
             Navigator.pushNamed(context,MyRoutes.screen2);
           }
        },
        items: [
          BottomNavigationBarItem(icon: Icon(Icons.home),label: 'home'),
          BottomNavigationBarItem(icon: Icon(Icons.menu_sharp),label: 'menu'),
        ],
      ),
    );
  }
}
