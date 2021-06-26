import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

import 'MyRoutes.dart';

class Screen2 extends StatefulWidget {
  const Screen2({Key key}) : super(key: key);

  @override
  _Screen2State createState() => _Screen2State();
}

class _Screen2State extends State<Screen2> {

  var listData;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    loadFolders();
  }

  loadFolders() async{
    var url1 = Uri.parse(MyVariables.folderDataUrl);
    print(url1);
    var response = await http.get(url1);
    if (response.statusCode == 200) {
        listData = convert.jsonDecode(response.body);
        setState(() {});
    }
    else{
      listData = [];
      setState(() {});
      print('please Check Your Internet Conn.');
    }
  }


  @override
  Widget build(BuildContext context) {
    var selectedItem = 1;
    return Scaffold(
      appBar: AppBar(title: Text('Movie Directory'),),
        body: (listData !=null && listData.isNotEmpty)? Container(
            child: ListView.builder(
                itemCount: listData.length,
                itemBuilder: (context, index) {
                  return MenuWidget( item:listData[index]);
                },
            ),):Center(
          child: CircularProgressIndicator(),
        ),
        bottomNavigationBar: BottomNavigationBar(
        currentIndex: selectedItem,
        onTap: (value) {
          selectedItem = value;
          setState(() {});
          if(selectedItem !=1){
            Navigator.pop(context);
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


class MenuWidget extends StatefulWidget {
  final item;

  const MenuWidget({Key key,@required this.item}) : super(key: key);

  @override
  _MenuWidgetState createState() => _MenuWidgetState();
}

class _MenuWidgetState extends State<MenuWidget> {
  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: () {
        print(widget.item);
        MyVariables.menuName = widget.item;
        Navigator.pushNamed(context, MyRoutes.menu);
      },
      child: Padding(
        padding: EdgeInsets.all(8.0),
        child: Card(
          clipBehavior: Clip.antiAlias,
            elevation: 10,
            child: Container(
              padding: EdgeInsets.all(20),
              alignment: Alignment.center,
                child: Text(widget.item,style: TextStyle(fontSize: 20),)
            )
        ),
      ),
    );
  }
}

