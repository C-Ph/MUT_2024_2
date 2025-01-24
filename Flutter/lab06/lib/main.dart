import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:uuid/uuid.dart';

void main() {
  runApp(const MyApp());
}

class Expense{
  String id;
  String title;
  String category;
  double amount;
  DateTime dateTime;

  Expense(
      {required this.title, required this.category, required this.amount, required this.dateTime}
      ): id = const Uuid().v4();
}

enum Category{
  FOOD,SHOPPING,TRANSPORT,ETC
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: ExpenseScreen(),
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
            icon: Icon(Icons.add,color: Colors.white,),
          ),
          IconButton(
            onPressed: () {},
            icon: Icon(Icons.settings,color: Colors.white,),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          _addExpense();
        },
        child: Icon(Icons.add),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Text('Total expense : '),
                Text('THB ${_calTotal()}'),
              ],
            ),
            const SizedBox(height: 20,),
            Expanded(
              child: ListView.builder(
                itemCount: _expenseList.length,
                itemBuilder: (context, index) {
                  final expense = _expenseList[index];
                  return Card(
                    child: ListTile(
                      title: Text(expense.title),
                      subtitle: Row(
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
    return _expenseList.fold(0, (acc, element) {
      return acc + element.amount;
    },);
  }

  void _addExpense() {

    String category = Category.SHOPPING.name;
    DateTime? datetime;

    final titleController = TextEditingController();
    final amountController = TextEditingController();

    showModalBottomSheet(context: context, builder: (context) {
      return StatefulBuilder(
        builder: (BuildContext context, void Function(void Function()) setState) {
          return Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Text('Add Expense',textAlign: TextAlign.center,),
                TextField(
                  controller: titleController,
                  decoration: InputDecoration(
                      hintText: 'Title',
                      border: OutlineInputBorder()
                  ),
                ),
                DropdownButton(
                  // items: [
                  //   DropdownMenuItem(
                  //       value: 'food',
                  //       child: Text('Food')
                  //   ),
                  //   DropdownMenuItem(
                  //       value: 'shopping',
                  //       child: Text('Shopping')
                  //   ),
                  // ],
                  value: category,
                  items: Category.values.map(
                        (e) => DropdownMenuItem(
                      value: e.name,
                      child: Text(e.name),
                    ),
                  ).toList(),
                  onChanged: (value) {
                    category = value!;
                  },
                ),
                TextField(
                  controller: amountController,
                  decoration: InputDecoration(
                      hintText: 'Amount',
                      border: OutlineInputBorder()
                  ),
                ),
                Row(
                  children: [
                    Text(datetime == null ?
                    'Not selected date':
                    DateFormat('dd/MM/yy').format(datetime!)
                    ),
                    IconButton(onPressed: () async {
                      final now = DateTime.now();
                      final selectedDate = await showDatePicker(
                          context : context,
                          firstDate: DateTime(now.year-1),
                          lastDate: DateTime(now.year,now.month+1)
                      );
                      setState(() {
                        datetime = selectedDate;
                      });
                    }, icon: Icon(Icons.calendar_month),
                    ),
                  ],
                ),
                ElevatedButton(
                  onPressed:(){
                    _expenseList.add(
                        Expense(
                            title: titleController.text,
                            category: category,
                            amount: double.parse(amountController.text),
                            dateTime: datetime!)
                    );
                    Navigator.of(context).pop();
                    this.setState(() {

                    });
                  } ,
                  child:  Text('ADD Expense'),
                )

              ],
            ),
          );
        },

      );
    },);
  }

}



