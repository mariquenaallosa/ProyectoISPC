import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, AbstractControl, FormControl } from '@angular/forms';
import { passwordMatch } from './validatorsPass';
import { Router } from '@angular/router';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {
  formRegistro = new FormGroup({
    nombre : new FormControl("", [Validators.required, Validators.maxLength(32)]),
    apellido : new FormControl("", [Validators.required, Validators.maxLength(32)]),
    email : new FormControl("", [Validators.required, Validators.email]),
    password : new FormControl("", [Validators.required, Validators.minLength(8)]),
    confirm_password : new FormControl("", [Validators.required, Validators.minLength(8)])

  }, [ passwordMatch("password", "confirm_password") ])

  getControl(name: any): AbstractControl | null {
    return this.formRegistro.get(name)
  }

  constructor(private router: Router){

  }
  registerFn(){
    if(this.formRegistro.valid){
      this.router.navigateByUrl('/users'),
      this.formRegistro.reset()
    }
    else{
      this.formRegistro.markAllAsTouched()
      alert('Error al ingresar los datos.')
    }
  }
  
  
  
  
}
