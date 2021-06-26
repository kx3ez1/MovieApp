import 'dart:ui';

class MyRoutes{
  static String menu = '/menu';
  static String screen1 = '/screen1';
  static String screen2 = '/screen2';
  static String splashScreen = '/spScreen';
  static String videoPlayer = '/vPlayer';
  static String teluguOld = '/tOld';
}


class MyVariables{
  static String androidId;
  static String msg1;
  static Brightness brightnessValue = Brightness.dark;
  static String videoName;
  static String videoUrl;
  static String rootHost = 'https://hhuu8.herokuapp.com/';
  static String folderDataUrl = 'https://hhuu8.herokuapp.com/menu';
  static String teluguOld = '$rootHost'+'latest';
  static String menuName = 'Latest';
  static String imageUrl(id1){
    return "http://www.jiorockerss.vin/details/Preview/$id1.jpg";
  }
  static String youtubeUrl = 'https://www.youtube.com/watch?v=2oR0COSr2L0';
}