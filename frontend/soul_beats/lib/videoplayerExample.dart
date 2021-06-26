import 'package:flutter/material.dart';
import 'package:flutter_web_browser/flutter_web_browser.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:soul_beats/MyRoutes.dart';
import 'package:video_viewer/domain/bloc/controller.dart';
import 'package:video_viewer/video_viewer.dart';
import 'package:mx_player_plugin/mx_player_plugin.dart';

import 'MyRoutes.dart';

class UsingVideoControllerExample extends StatefulWidget {

  UsingVideoControllerExample({Key key}) : super(key: key);

  @override
  _UsingVideoControllerExampleState createState() =>  _UsingVideoControllerExampleState();
}

class _UsingVideoControllerExampleState extends State<UsingVideoControllerExample> {
  final VideoViewerController controller1 = VideoViewerController();

  _openInMx() async{
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Playing With Mx',style: TextStyle(fontSize: 16,)),backgroundColor: Colors.red,));
    await PlayerPlugin.openWithMxPlayer(MyVariables.videoUrl, MyVariables.videoUrl);
  }
  _openInVlc() async{
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Playing With VLC',style: TextStyle(fontSize: 16,)),backgroundColor: Colors.red,));
    await PlayerPlugin.openWithVlcPlayer(MyVariables.videoUrl);
  }
  _openBrowserTab() async {
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text('Playing With Browser',style: TextStyle(fontSize: 16,)),backgroundColor: Colors.red,));
    await FlutterWebBrowser.openWebPage(url: MyVariables.videoUrl,customTabsOptions: CustomTabsOptions(showTitle: false,toolbarColor: Colors.red,urlBarHidingEnabled: true,secondaryToolbarColor: Colors.red));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: SingleChildScrollView(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            mainAxisSize: MainAxisSize.max,
            children: [
              SizedBox(height: 5,),
              Padding(padding: EdgeInsets.all(16.0),
                child: VideoViewer(
                  controller: controller1,
                  onFullscreenFixLandscape: true,
                  source: {
                    MyVariables.videoName : VideoSource(
                      video: VideoPlayerController.network(MyVariables.videoUrl),
                    )
                  },
                ),
              ),
              Padding(
                padding: const EdgeInsets.all(18.0),
                child: Text(MyVariables.videoName,style: TextStyle(fontSize: 20,),),
              ),
              Text('Playing Sources'),
              Divider(
                color: Colors.red,
              ),
              Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    ElevatedButton(
                        onPressed:_openInMx,
                        style: ButtonStyle(elevation: MaterialStateProperty.all(10),backgroundColor: MaterialStateProperty.all(Colors.red)),
                        child: Text('MX player')),
                    ElevatedButton(
                        style: ButtonStyle(elevation: MaterialStateProperty.all(10),backgroundColor: MaterialStateProperty.all(Colors.red)),
                        onPressed:_openInVlc,
                        child: Text('VLC')),
                    ElevatedButton(
                      style: ButtonStyle(elevation: MaterialStateProperty.all(10),backgroundColor: MaterialStateProperty.all(Colors.red)),
                      onPressed:_openBrowserTab,
                      child: Text('Chrome'),
                    ),
                  ],
                ),
              Divider(
                color: Colors.red,
              ),
            ],
          ),
      ),
      );
  }
}