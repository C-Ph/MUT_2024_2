import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:lab07/setting.dart';
import 'package:uuid/uuid.dart';

void main() {
  runApp(const Myapp());
}

class Expense {
  String id;
  String title;
  double amount;
  String category;
  DateTime dateTime;

  Expense(
      {required this.title,
        required this.amount,
        required this.category,
        required this.dateTime})
      : id = const Uuid().v4();
}

enum Category { FOOD, SHOPPING, TRANSPORT, ETC }

class Myapp extends StatelessWidget {
  const Myapp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
            seedColor: Colors.green,
            brightness: Brightness.light,

       ),
      ),
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
    Expense(
        title: 'dinner',
        amount: 500,
        category: Category.FOOD.name,
        dateTime: DateTime(2024, 12, 10)),
    Expense(
        title: 'bts',
        amount: 120,
        category: Category.TRANSPORT.name,
        dateTime: DateTime(2024, 12, 5)),
    Expense(
        title: 'gift',
        amount: 300,
        category: Category.SHOPPING.name,
        dateTime: DateTime(2024, 12, 5)),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        title: Text(
          'Extense Tracker',
         // style: TextStyle(color: Colors.white),
        ),
        actions: [
          IconButton(
            onPressed: () {
              _addExpense();
            },
            icon: Icon(
              Icons.add,

            ),
          ),
          IconButton(
            onPressed: () {
              Navigator.of(context).push(
                MaterialPageRoute(builder: (context) => SettingScreen(),)
              );
            },
            icon: Icon(
              Icons.settings,

            ),
          )
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
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                Text('Total Extense :'),
                Text('${_calTotal()} THB'),
              ],
            ),
            SizedBox(
              height: 20,
            ),
            Expanded(
              child: ReorderableListView.builder(
                onReorder: (oldIndex, newIndex) {
                  setState(() {
                    
                  });
                },
                itemCount: _expenseList.length,
                itemBuilder: (context, index) {
                  final expense = _expenseList[index];
                  return Dismissible(
                    onDismissed: (direction) {
                      setState(() {
                        _expenseList.removeAt(index);
                      });
                      ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(
                            content:Text('${expense.title} was deleted'),
                            action: SnackBarAction(
                              label: 'Undo',
                              onPressed: (){
                                setState(() {
                                  _expenseList.insert(index, expense);
                                });


                            },),
                          )
                      );
                    },
                    direction: DismissDirection.endToStart,
                    background: Container(
                      color: Colors.red,
                      child: Icon(Icons.delete_forever),
                      alignment: Alignment.centerRight,
                      padding: EdgeInsets.all(10),
                    ),
                    key: ValueKey(expense.id),
                    child: Card(
                      child: ListTile(
                        onTap: () {
                          _addExpense(expense);
                        },
                        title: Text(expense.title),
                        subtitle: Row(
                          children: [
                            Text(
                                '${DateFormat('dd/MM/yy').format(expense.dateTime)}'),
                            SizedBox(
                              width: 10,
                            ),
                            Text('${expense.category}'),
                          ],
                        ),
                        trailing: Text('${expense.amount}'),
                      ),
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
    return _expenseList.fold(
      0,
          (acc, element) {
        return acc + element.amount;
      },
    );
  }

  void _addExpense([Expense? expense]) {
    //String _title;
    String _category = Category.SHOPPING.name;
    DateTime? _datetime;
    //double _amount;

    final _titleController = TextEditingController();
    final _amountController = TextEditingController();

    // if exists assign to local variable
    if (expense != null) {
      _titleController.text = expense.title;
      _amountController.text = expense.amount.toStringAsFixed(2);
      _category = expense.category;
      _datetime = expense.dateTime;
    }
    showModalBottomSheet(
      context: context,
      builder: (context) {
        return StatefulBuilder(
          builder:
              (BuildContext context, void Function(void Function()) setState) {
            return Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(
                    expense==null?'Add Expense':'Edit Expense',
                    textAlign: TextAlign.center,
                  ),
                  TextField(
                    controller: _titleController,
                    decoration: InputDecoration(
                        hintText: 'Title', border: OutlineInputBorder()),
                  ),
                  DropdownButton(
                    // items: [
                    //   DropdownMenuItem(
                    // value: 'Food',
                    // child: Text('Food')
                    //   ),
                    //   DropdownMenuItem(
                    //       value: 'shopping',
                    //       child: Text('Shopping')
                    //   ),
                    // ],
                      value: _category,
                      items: Category.values
                          .map(
                            (e) => DropdownMenuItem(
                          value: e.name,
                          child: Text(e.name),
                        ),
                      )
                          .toList(),
                      onChanged: (value) {
                        _category = value!;
                      }),
                  TextField(
                    controller: _amountController,
                    decoration: InputDecoration(
                        hintText: 'Amount', border: OutlineInputBorder()),
                  ),
                  Row(
                    children: [
                      Text(_datetime == null
                          ? 'No Selected Date'
                          : DateFormat('dd/MM/yy').format(_datetime!)),
                      IconButton(
                        onPressed: () async {
                          final now = DateTime.now();
                          final selecteddate = await showDatePicker(
                              context: context,
                              initialDate: now,
                              firstDate: DateTime(now.year - 1),
                              lastDate: DateTime(now.year, now.month + 1));
                          setState(() {
                            _datetime = selecteddate;
                          });
                        },
                        icon: Icon(Icons.calendar_month),
                      ),
                    ],
                  ),
                  ElevatedButton(
                    onPressed: () {

                      if (expense == null) {
                        _expenseList.add(Expense(
                            title: _titleController.text,
                            amount: double.parse(_amountController.text),
                            category: _category,
                            dateTime: _datetime!));

                      }
                      else {
                        expense.title = _titleController.text;
                        expense.amount = double.parse(_amountController.text);
                        expense.category = _category;
                        expense.dateTime = _datetime!;
                      }
                      Navigator.of(context).pop();
                      this.setState(() {});
                    },
                    child: Text(expense==null?'Add Expense':'Edit Expense'),
                  )
                ],
              ),
            );
          },
        );
      },
    );
  }
}
