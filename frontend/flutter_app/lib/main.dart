import 'package:flutter/material.dart';

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
  double fireProb = 10.0;

  Color pickColor(double prob) {
    if (prob < 3.0)
      return Colors.green;
    if (prob < 7.0)
      return Colors.yellow;

    return Colors.red;
  }

  @override
  Widget build(BuildContext context) {
    return Text(
      fireProb.toString(),
      style: TextStyle(
        fontWeight: FontWeight.bold,
        fontSize: 30.0,
        color: pickColor(fireProb),
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
