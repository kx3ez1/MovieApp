import 'package:carousel_slider/carousel_slider.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:soul_beats/MyRoutes.dart';
import 'package:soul_beats/videoplayerExample.dart';
import 'dart:convert' as convert;
import 'package:http/http.dart' as http;
import 'package:video_viewer/domain/bloc/controller.dart';
import 'package:video_viewer/video_viewer.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';

import 'DrawerCode.dart';



class TeluguOld extends StatefulWidget {



  final urlForData;
  const TeluguOld({Key key,@required this.urlForData}) : super(key: key);

  @override
  _TeluguOldState createState() => _TeluguOldState();
}

class _TeluguOldState extends State<TeluguOld> {
  final key1 = GlobalKey();

  var selectedItem = 0;       //bottom nav


  Future<void> _showSearch() async {
    await showSearch(
      context: context,
      delegate: TheSearch(),
      query: "",
    );
  }


  var count;
  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    request2(widget.urlForData);
  }

  request2(String url) async {
    var url1 = Uri.parse(url);
    print(url1);
      var response = await http.get(url1);
      if (response.statusCode == 200) {
        var jsonData = convert.jsonDecode(response.body);
        Telugu2001Data.items = List.from(jsonData).map<Telugu2001>((item) => Telugu2001.fromJson(item)).toList();
        setState(() {});
      }
      else{
        print('error occurred');
      }
    }

  // @override
  // Widget build(BuildContext context) {
  //   return Scaffold(
  //       appBar: AppBar(title: Text(MyVariables.menuName),),
  //       body: (Telugu2001Data.items!=null && Telugu2001Data.items.isNotEmpty)? Container(
  //         child: ListView.builder(
  //           itemCount: Telugu2001Data.items?.length ?? 0,
  //           itemBuilder: (context, index) {
  //             return MovieCardItemWidget(
  //               item: Telugu2001Data.items[index],
  //             );
  //           },
  //         ),
  //       ):Center(
  //           child: CircularProgressIndicator(),
  //       )
  //   );
  // }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text(MyVariables.menuName),
        actions:[
          IconButton(
            icon: Icon(Icons.search),
            onPressed: _showSearch,
          ),
        ],),
        body: (Telugu2001Data.items!=null && Telugu2001Data.items.isNotEmpty)? Container(
          key: key1,
          child: GridView.builder(
            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: MediaQuery.of(context).orientation == Orientation.landscape? 3:2,
              childAspectRatio: 0.5
            ),
            itemCount: Telugu2001Data.items?.length ?? 0,
            itemBuilder: (context, index) {
              return MovieCardItemWidgetTest(
                item: Telugu2001Data.items[index],
              );
            },
          )
        ):Center(
          child: CircularProgressIndicator(),
        ),
      drawer: DrawerCode(),
    );
  }
}


class MovieCardItemWidgetTest extends StatelessWidget {
  final Telugu2001 item;
  static VideoViewerController controller1 = VideoViewerController();

  const MovieCardItemWidgetTest({Key key,@required this.item}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final imageUrl = item.id;
    return InkWell(
      onTap: () {
        MyVariables.videoName = item.name;
        MyVariables.videoUrl = item.url;
        Navigator.pushNamed(context, MyRoutes.videoPlayer);
      },
      child: Card(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            //Image.network('http://www.jiorockerss.vin/details/Preview/$imageUrl.jpg',fit: BoxFit.cover,height: 350,),
            Image.network('http://www.jiorockerss.vin/details/Preview/$imageUrl.jpg',fit: BoxFit.cover,height: 300,errorBuilder: (context, error, stackTrace) {
              return Image.network(
                  'http://www.jiorockerss.vin/details/Preview/${imageUrl -
                      1}.jpg', fit: BoxFit.cover,
                  height: 300,
                  errorBuilder: (context, error, stackTrace) {
                    return Image.network(
                        'http://www.jiorockerss.vin/details/Preview/${imageUrl +
                            1}.jpg', fit: BoxFit.cover,
                        height: 300,
                        errorBuilder: (context, error, stackTrace) {
                          if(imageUrl != null) {
                            return Image.network(
                              'http://www.jiorockerss.vin/details/Screenshots/${imageUrl}/${imageUrl}a.jpg', fit: BoxFit.cover, height: 300,
                              errorBuilder: (context, error, stackTrace) {
                                return Text('no image');
                              },
                            );
                          }
                              else{
                                return Text('no image');
                          }
                          }
                    );
                  }
              );
            }),
            Text(item.name,style: TextStyle(
              fontSize: 16
            ),
    ),
          ]
        ),
      ),
    );
  }
  }

class MovieCardItemWidget extends StatelessWidget {
  final Telugu2001 item;
  static VideoViewerController controller1 = VideoViewerController();

  const MovieCardItemWidget({Key key,@required this.item}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final imageUrl = item.id;
    return SingleChildScrollView(
      child: Padding(
        padding: EdgeInsets.all(10.0),
        child: Card(
          elevation: 16,
          child: InkWell(
            onTap: () {
              MyVariables.videoName = item.name;
              MyVariables.videoUrl = item.url;
              Navigator.pushNamed(context, MyRoutes.videoPlayer);
              },
              child: Container(
                decoration: BoxDecoration(
                  //image: DecorationImage(image: NetworkImage('http://www.jiorockerss.vin/details/Screenshots/${imageUrl}/${imageUrl}a.jpg'),fit: BoxFit.cover),
                ),
                padding: EdgeInsets.all(10),
                child: Column(
                    children:[
                      Image.network('http://www.jiorockerss.vin/details/Screenshots/${imageUrl}/${imageUrl}a.jpg',fit: BoxFit.cover,),
                      SizedBox(height: 5,),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(item.name,style: TextStyle(fontSize: 16),),
                      ),
              ]
                )
              ),
            ),
        )
      ),
    );
  }
}


class Telugu2001Data{
  static List<Telugu2001> items;
}

class Telugu2001 {
    int id;
    String name;
    RootId root_id;
    String type;
    String url;

    Telugu2001({this.id, this.name, this.root_id, this.type, this.url});

    factory Telugu2001.fromJson(Map<String, dynamic> json) {
        return Telugu2001(
            id: json['id'],
            name: json['name'],
            root_id: json['root_id'] != null ? RootId.fromJson(json['root_id']) : null,
            type: json['type'],
            url: json['url'],
        );
    }

    Map<String, dynamic> toJson() {
        final Map<String, dynamic> data = new Map<String, dynamic>();
        data['id'] = this.id;
        data['name'] = this.name;
        data['type'] = this.type;
        data['url'] = this.url;
        if (this.root_id != null) {
            data['root_id'] = this.root_id.toJson();
        }
        return data;
    }
}

class RootId {
    String oid;

    RootId({this.oid});

    factory RootId.fromJson(Map<String, dynamic> json) {
        return RootId(
            oid: json['oid'],
        );
    }

    Map<String, dynamic> toJson() {
        final Map<String, dynamic> data = new Map<String, dynamic>();
        data['oid'] = this.oid;
        return data;
    }
}



class TheSearch extends SearchDelegate<String> {
  TheSearch({this.contextPage});

  BuildContext contextPage;

  @override
  String get searchFieldLabel => "2021,Bahubali";

  @override
  List<Widget> buildActions(BuildContext context) {
    return [
      IconButton(
        icon: Icon(Icons.clear),
        onPressed: () {
          query = "";
          SuggestedMovieDataList.items = [];
          SuggestedMovieDataList.itemsResult = [];
        },
      )
    ];
  }

  @override
  Widget buildLeading(BuildContext context) {
    return IconButton(
      icon: AnimatedIcon(
        icon: AnimatedIcons.menu_arrow,
        progress: transitionAnimation,
      ),
      onPressed: () {
        close(context, null);
      },
    );
  }

  @override
  Widget buildResults(BuildContext context) {

    request4(query) async {
      var url1 = Uri.parse('https://hhuu8.herokuapp.com/search?q=$query');
      print(url1);
      var response = await http.get(url1);
      if (response.statusCode == 200) {
        var suggest = convert.jsonDecode(response.body);
        SuggestedMovieDataList.items = List.from(suggest).map<SuggestedMovieData>((item) => SuggestedMovieData.fromJson(item)).toList();
        for(var i=0;i<SuggestedMovieDataList.items.length;i++){
          print(SuggestedMovieDataList.items[i].name);
        }
        return SuggestedMovieDataList.items;
      }
      else{
        return [];
      }
    }

    reqData1(query){
      request4(query);
      return SuggestedMovieDataList.items;
    }

    final suggestions = query.isEmpty?reqData1('bahubali'):reqData1(query);
    print(suggestions.length);
    return (suggestions!=null && suggestions.isNotEmpty)? GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 0.5,
        ),
        itemCount: suggestions?.length ?? 0,
        itemBuilder: (content, index) => InkWell(
          onTap: () {
            MyVariables.videoName = suggestions[index].name;
            MyVariables.videoUrl = suggestions[index].url;
            Navigator.pushNamed(context, MyRoutes.videoPlayer);
          },
          child: Card(
            child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Image.network(MyVariables.imageUrl(suggestions[index].id),fit: BoxFit.cover,height: 300,errorBuilder: (context, error, stackTrace) {
                    return Text('No Image');
                  }),
                  Text(suggestions[index].name,style: TextStyle(
                      fontSize: 16
                  ),),
                ]
            ),
          ),
        )
    ):Text('No Results Found',style: TextStyle(fontSize: 20),);

  }


  @override
  Widget buildSuggestions(BuildContext context) {

     
    request3(query) async {
      var url1 = Uri.parse('https://hhuu8.herokuapp.com/search?q=$query');
      print(url1);
      var response = await http.get(url1);
      if (response.statusCode == 200) {
        var suggest = convert.jsonDecode(response.body);
        SuggestedMovieDataList.items = List.from(suggest).map<SuggestedMovieData>((item) => SuggestedMovieData.fromJson(item)).toList();
        for(var i=0;i<SuggestedMovieDataList.items.length;i++){
          print(SuggestedMovieDataList.items[i].name);
        }
        return SuggestedMovieDataList.items;
        }
      else{
        return [];
      }
    }

    reqData(query){
      request3(query);
      return SuggestedMovieDataList.items;
    }

    final suggestions = query.isEmpty?reqData('avunu'):reqData(query);
    return (suggestions!=null && suggestions.isNotEmpty)? GridView.builder(
        gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 0.5,
        ),
      itemCount: suggestions?.length ?? 0,
      itemBuilder: (content, index) => InkWell(
        onTap: () {
          MyVariables.videoName = suggestions[index].name;
          MyVariables.videoUrl = suggestions[index].url;
          Navigator.pushNamed(context, MyRoutes.videoPlayer);
        },
        child: Card(
    child: Column(
    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            Image.network(MyVariables.imageUrl(suggestions[index].id),fit: BoxFit.cover,height: 300,errorBuilder: (context, error, stackTrace) {
              return Text('No Image');
            }),
            Text(suggestions[index].name,style: TextStyle(
                fontSize: 16
            ),),
          ]
    ),
    ),
      )
    ):Text('No Results Found',style: TextStyle(fontSize: 20),);
}
}

class SuggestedMovieData {
    int id;
    String name;
    String type;
    String url;

    SuggestedMovieData({this.id, this.name, this.type, this.url});

    factory SuggestedMovieData.fromJson(Map<String, dynamic> json) {
        return SuggestedMovieData(
            id: json['id'],
            name: json['name'],
            type: json['type'],
            url: json['url'],
        );
    }

    Map<String, dynamic> toJson() {
        final Map<String, dynamic> data = new Map<String, dynamic>();
        data['id'] = this.id;
        data['name'] = this.name;
        data['type'] = this.type;
        data['url'] = this.url;
        return data;
    }
}

class SuggestedMovieDataList{
  static List<SuggestedMovieData> items;
  static List<SuggestedMovieData> itemsResult;
}
