import 'package:flutter/material.dart';
import 'package:uuid/uuid.dart';
import 'package:intl/intl.dart';

void main() {
  runApp(const MyApp());
}

class Expense{
  String id;
  String title;
  String category;
  double amount;
  DateTime dateTime;

  Expense({required this.title, required this.category, required this.amount, required this.dateTime}
      ):id = Uuid().v4();

}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: const ExpenseScreen(),
    );
  }
}

class ExpenseScreen extends StatefulWidget {
  const ExpenseScreen({super.key});

  @override
  State<ExpenseScreen> createState() => _ExpenseScreenState();
}

class _ExpenseScreenState extends State<ExpenseScreen> {

  final _expenseList = [
    // Test
    Expense(title: 'dinner', category: 'food', amount: 500, dateTime: DateTime(2024,12,10)),
    Expense(title: 'bts', category: 'transport', amount: 120, dateTime: DateTime(2024,12,5)),
    Expense(title: 'gift', category: 'shopping', amount: 300, dateTime: DateTime(2024,12,2)),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: const Text(
          'Expense Tracker',
          style: TextStyle(
            color: Colors.white,
          ),
        ),
        actions: [
          IconButton(
            onPressed: () {},
            icon: const Icon(
              Icons.add,
              color: Colors.white,
            ),
          ),
          IconButton(
            onPressed: () {},
            icon: const Icon(
              Icons.settings,
              color: Colors.white,
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: const Icon(Icons.add),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              // mainAxisAlignment: MainAxisAlignment.spaceAround,
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Text('Total expense : '),
                Text('THB ${_calTotal()}'),
              ],
            ),
            const SizedBox(height: 20),
            Expanded(
              child: ListView.builder(
                itemCount: _expenseList.length,
                itemBuilder: (context, index) {
                  final expense = _expenseList[index];
                  return Card(
                    child: ListTile(
                      title: Text('${expense.title}'),
                      subtitle : Row(
                        children: [
                          Text('${DateFormat('dd/MM/yy').format(expense.dateTime)}'),
                          SizedBox(width: 10,),
                          Text('${expense.category}'),
                        ],
                      ),
                      trailing: Text('${expense.amount}'),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }

  double _calTotal() {
    return _expenseList.fold(0.0, (acc, expense) {
      return acc + expense.amount;
    });
  }

}
