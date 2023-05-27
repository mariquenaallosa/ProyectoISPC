import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  
  get email(){
    return this.formLogin.get('email') as FormControl;
  }
  get password(){
    return this.formLogin.get('password') as FormControl;
  }
  
  formLogin= new FormGroup({
    'email': new FormControl ('', [Validators.required, Validators.email]),
    'password': new FormControl('',Validators.required),
  })

}
