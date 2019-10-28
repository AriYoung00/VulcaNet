import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

import 'graph_view.dart';

const String url = "http://192.168.43.189:1234";
const String url_eduroam = "http://169.228.184.139:1234";

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'VulcaNet',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'VulcaNet'),
    );
  }
}

class FireProb extends StatefulWidget {
  @override
  _FireProbState createState() => _FireProbState();
}

class _FireProbState extends State<FireProb> {
  String data;
  double fireProb = 0.0;

  @override
  void initState() {
    super.initState();
    const delay = const Duration(seconds: 1);
    new Timer.periodic(delay, (Timer t) => getProb());
  }

  Future<String> getProb() async {
    var res = await http.post(
      Uri.encodeFull(url + "/fire/get_prob/"),
      //headers: {"Content-type": "application/json"}
    );

    setState(() {
      data = (res.body);
    });

    return "Success";
  }

  void setFireProb(String data) {
    if (data != null && data.length >= 1)
      fireProb = double.parse(data);
  }

  Color pickColor(double prob) {
    if (prob < 30.0)
      return Colors.green;
    if (prob < 70.0)
      return Colors.yellow;

    return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
//    getProb();
    setFireProb(data);

    return Text(
      data,
      style: TextStyle(
        fontWeight: FontWeight.bold,
        fontSize: 30.0,
        color: pickColor((fireProb)),
      ),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String sensorNum = "0";
  List<dynamic> sensorList = [];

  @override
  void initState() {
    super.initState();
    const delay = const Duration(seconds: 1);
    new Timer.periodic(delay, (Timer t) => getSensorsNum());
    new Timer.periodic(delay, (Timer t) => getSensors());
  }

  Future<String> getSensorsNum() async {
    var res = await http.get(
      Uri.encodeFull(url + "/sensors/active_num/"),
    );

    setState(() {
      sensorNum = (res.body);
    });

    print("SENSOR NUMBER");
    print(sensorNum);
    return "Success";
  }

  Future<String> getSensors() async {
    var res = await http.post(
      Uri.encodeFull(url + "/sensors/list/"),
      headers: {"Content-type": "application/json"}
    );

    setState(() {
      sensorList = json.decode(res.body)['dataTypes'];
    });
    print("SENSOR LIST");
    print(sensorList);
    return "Success";
  }

  Widget buildBody(BuildContext ctxt, int index) {
    return new Center(child: Text(sensorList[index]));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Container(
        padding: const EdgeInsets.only(top:30.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget> [
                Text(
                  'Fire Danger: ',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 30.0,
                  ),
                ),
                FireProb(),
              ]
            ),
            Container(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Text(
                    'Active Sensors:',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 20.0,
                    ),
                  ),
                  SizedBox(
                    height: 50,
                    child: ListView.builder(
                      itemCount: int.parse(sensorNum),
                      itemBuilder: (BuildContext ctxt, int index) => buildBody(ctxt, index),
                    ),
                  ),
                ],
              )
            ),
            RaisedButton(
              child: Text('Manage Sensors'),
              padding: EdgeInsets.fromLTRB(10, 10, 10, 10),
              color: Colors.blue,
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (context) => GraphView()),
                );
              },
            )
          ],
        ),
      ),
    );
  }
}
