import 'package:flutter/material.dart';
import 'package:form_field_validator/form_field_validator.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  static const url =
      'https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg?format=1500w';

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final email_text_control = TextEditingController();
  final password_text_control = TextEditingController();

  final passwordValidator = MultiValidator([
    RequiredValidator(errorText: 'password is required'),
    MinLengthValidator(8, errorText: 'password must be at least 8 digits long'),
    PatternValidator(r'(?=.*?[#?!@$%^&*-])',
        errorText: 'passwords must have at least one special character')
  ]);

  // String error_text = 'No Error';
  final error_text_control = TextEditingController();
  final from_key = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Form(
        key: from_key,
        child: Container(
            margin: EdgeInsets.all(28),
            width: double.infinity,
            child: Column(
              children: [
                Stack(children: [
                  Image.network(
                    LoginScreen.url,
                    height: 150,
                    width: double.infinity,
                    fit: BoxFit.cover,
                  ),
                  const Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      Text(
                        'Already Have an Account?',
                        style: TextStyle(color: Colors.white, fontSize: 20),
                      ),
                      Icon(Icons.person, size: 100)
                    ],
                  ),
                ]),
                SizedBox(
                  height: 20,
                ),
                // Text(error_text, style: TextStyle(color: Colors.red)),
                TextFormField(
                  validator: EmailValidator(errorText: 'Please Input Email'),
                  controller: email_text_control,
                  decoration: InputDecoration(
                      prefixIcon: Icon(Icons.email),
                      hintText: 'Email',
                      border: OutlineInputBorder(
                          borderRadius:
                          BorderRadius.all(Radius.circular(20.0)))),
                ),
                SizedBox(
                  height: 20,
                ),
                TextFormField(
                  validator: passwordValidator,
                  controller: password_text_control,
                  obscureText: true,
                  decoration: InputDecoration(
                      prefixIcon: Icon(Icons.lock),
                      hintText: 'Password',
                      border: OutlineInputBorder(
                          borderRadius:
                          BorderRadius.all(Radius.circular(20.0)))),
                ),
                SizedBox(
                  height: 20,
                ),
                Container(
                  height: 40,
                  width: double.infinity,
                  child: ElevatedButton(
                    onPressed: () {
                      from_key.currentState?.validate();
                    },
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blue,
                      foregroundColor: Colors.white,
                    ),
                    child: const Text('LOGIN'),
                  ),
                ),
                SizedBox(
                  height: 20,
                ),
                Text("Sign Up")
              ],
            )));
  }
}