import 'dart:convert';

import 'dart:math';
import 'package:flutter/material.dart';
import 'package:soul_beats/MyRoutes.dart';
import 'package:soul_beats/screen1.dart';
import 'package:soul_beats/screen2.dart';
import 'package:soul_beats/splashScreen.dart';
import 'package:soul_beats/teluguold.dart';
import 'package:soul_beats/videoplayerExample.dart';
import 'package:device_info/device_info.dart';
import 'package:http/http.dart' as http;

import 'menu.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {


  @override
  _MyAppState createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> with WidgetsBindingObserver {



  @override
  void initState() {
    // TODO: implement initState
    super.initState();


    WidgetsBinding.instance.addObserver(this);

  }

  getDeviceInfo() async{
    DeviceInfoPlugin deviceInfo = DeviceInfoPlugin();
    AndroidDeviceInfo androidInfo = await deviceInfo.androidInfo;
    // print('physical on ${androidInfo.isPhysicalDevice}');
    // print('androidId on ${androidInfo.androidId}');
    // print('display on ${androidInfo.display}');
    // print('systemFeature on ${androidInfo.systemFeatures}');
    // print('manufacturer on ${androidInfo.manufacturer}');
    // print('Model on ${androidInfo.model}');
    // print('Brand on ${androidInfo.brand}');

    var id1rr = "";

    String requestIdSecure() {
      String generateRandomString(int len) {
        var r = Random();
        const _chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890';
        return List.generate(len, (index) => _chars[r.nextInt(_chars.length)])
            .join();
      }
      var rtt = [0, 1, 4, 5, 6, 8, 9];
      Random rd = Random();
      final val666 = rtt[rd.nextInt(rtt.length)].toString();
      final val667 = rtt[rd.nextInt(rtt.length)].toString();
      final val668 = rtt[rd.nextInt(rtt.length)].toString();
      final val669 = rtt[rd.nextInt(rtt.length)].toString();
      final val670 = rtt[rd.nextInt(rtt.length)].toString();
      final val671 = rtt[rd.nextInt(rtt.length)].toString();
      final st1_1 = val666 + val667 + val668 + val669 + val670 + val671;
      final st1_2 = generateRandomString(10);
      final st1_3 = generateRandomString(10);
      final st1 = "\$$st1_3-$st1_2-$st1_1";
      return st1;
    }

    var secureId = requestIdSecure();

    var url1 = Uri.parse('https://userhhuu8.herokuapp.com/user/$secureId');

    await http.post(url1,body: jsonEncode(
        {"time": DateTime.now().toString(),
      "deviceId": androidInfo.androidId,
      "brand":androidInfo.brand+' '+androidInfo.model,
      "physicalDevice":androidInfo.isPhysicalDevice,
      "status": _notification.toString(),

    }));
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }
  AppLifecycleState _notification;

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    setState(() {
      _notification = state;
    });
    getDeviceInfo();
  }



  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      themeMode: ThemeMode.system,
      theme: ThemeData(
        brightness: Brightness.light,
        primaryColor: Colors.red,
        pageTransitionsTheme: PageTransitionsTheme(
            builders: {
              TargetPlatform.android: CupertinoPageTransitionsBuilder(),
              TargetPlatform.iOS: CupertinoPageTransitionsBuilder(),
            }
        )
      ),
      darkTheme: ThemeData(
        brightness: Brightness.dark,
      ),
      routes: {
        MyRoutes.menu:(context) => MenuApp1(),
        MyRoutes.screen1:(context) => Screen1(),
        MyRoutes.screen2:(context) => Screen2(),
        MyRoutes.splashScreen:(context) => SplashScreen(),
        MyRoutes.videoPlayer:(context) => UsingVideoControllerExample(),
        MyRoutes.teluguOld:(context) => TeluguOld(),
      },
      initialRoute: MyRoutes.splashScreen,
    );
  }
}