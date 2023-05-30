import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  formLogin=this.formBuilder.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', Validators.required],
  })

  constructor(private formBuilder:FormBuilder, private router:Router){
    
  }

  get email(){
    return this.formLogin.get('email') as FormControl;
  }

  get password(){
    return this.formLogin.get('password') as FormControl;
  }

  login(){
    if(this.formLogin.valid){
      console.log('llamar al servicio de login')
      this.router.navigateByUrl('/users'),
      this.formLogin.reset()
    }
    else{
      this.formLogin.markAllAsTouched()
      alert('Error al ingresar los datos.')
    }
  }

  

}
