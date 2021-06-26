import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:soul_beats/MyRoutes.dart';
import 'package:url_launcher/url_launcher.dart';


class DrawerCode extends StatefulWidget {
  const DrawerCode({Key key}) : super(key: key);


  @override
  _DrawerCodeState createState() => _DrawerCodeState();
}

class _DrawerCodeState extends State<DrawerCode> {


  _openYt() async{
    await launch(MyVariables.youtubeUrl,forceSafariVC: false);
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      elevation: 10,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Text('All Credits To Jiorockerss.vin'),
          //Image.asset('assets/soulbeatslogo.jpg',fit: BoxFit.cover,),
          Column(
            children: [
              Text('Thank You'),
              Divider(color: Colors.black,indent: 15,endIndent: 15,thickness: 2,),
              Text('SoulBeats™',style: TextStyle(fontSize: 30),),
              Divider(color: Colors.black,indent: 15,endIndent: 15,thickness: 2,),
            ],
          ),
          Column(
            children: [
              Text('Please subscribe',style: TextStyle(fontSize: 20),),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Column(
                    children: [
                      IconButton(
                          tooltip: 'SoulBeats',
                          color: Colors.red,
                          iconSize: 54,
                          icon: FaIcon(FontAwesomeIcons.youtube,),
                          onPressed:_openYt
                      ),
                      Text('Youtube',style: TextStyle(),),
                    ],
                  ),
                  Column(
                    children: [
                      IconButton(
                          tooltip: 'SoulBeats',
                          color: Colors.lightBlue,
                          iconSize: 54,
                          icon: FaIcon(FontAwesomeIcons.telegram),
                          onPressed: () {
                            showDialog(context: context, builder: (context) {
                              return AlertDialog(title: Text('Only Youtube'));
                            },);
                          }
                      ),
                      Text('Telegram',style: TextStyle(),)
                    ],
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
    );
  }
}
