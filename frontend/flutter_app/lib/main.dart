import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';

import 'graph_view.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'FireMesh',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'FireMesh'),
    );
  }
}

class FireProb extends StatefulWidget {
  @override
  _FireProbState createState() => _FireProbState();
}

class _FireProbState extends State<FireProb> {
  String url = "http://192.168.43.189:1234/fire/get_prob/";
  String data;
  double fireProb = 0.0;

  Future sleep5() {
    return new Future.delayed(const Duration(seconds:10));
  }

  Future<String> getProb() async {
    var res = await http.post(
      Uri.encodeFull(url),
      //headers: {"Content-type": "application/json"}
    );

    setState(() {
      data = (res.body);
    });

    new Future.delayed(const Duration(seconds: 10));
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
    getProb();
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
            RaisedButton(
              child: Text('Sensor Data'),
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
