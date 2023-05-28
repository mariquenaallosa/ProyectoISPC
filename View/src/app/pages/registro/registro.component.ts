import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent {
  form!:FormGroup;

  constructor(private fb:FormBuilder){
    this.registro();
  }

  get nombreNovalido(){
    return this.form.get('nombre')?.invalid && this.form.get('nombre')?.touched;
  }
  get apellidoNovalido(){
    return this.form.get('apellido')?.invalid && this.form.get('apellido')?.touched;
  }
  get emailNovalido(){
    return this.form.get('email')?.invalid && this.form.get('email')?.touched
  }
  get password1Novalido(){
    return this.form.get('password1')?.invalid && this.form.get('password1')?.touched;
  }
  get password2Novalido(){
    return this.form.get('password2')?.invalid && this.form.get('password2')?.touched;
  }

  registro(){
    this.form= this.fb.group({
      nombre:['', Validators.required],
      apellido:['', Validators.required],
      email:['', [Validators.required, Validators.email]],
      password1: ['', [Validators.required,Validators.minLength(8)]],
      password2: ['', Validators.required],

    },{
    Validators:this.passwordIguales('password1', 'password2'),
    })
  }

  btnRegistro(){
    console.log(this.form);
    this.passNovalido();

    if (this.form.invalid){
      return Object.values(this.form.controls).forEach(control=>{
        control.markAllAsTouched();
      })
    }
  }

  passNovalido(){
    const pass1= this.form.get('password1')?.value;
    const pass2= this.form.get('password2')?.value;

    if (pass1 !== pass2){
      return true;
    }else{
      return false;
    }
  }

  passwordIguales(pass1Name:string, pass2Name:string){
    return (formGroup:FormGroup) =>{
      const pass1Control = formGroup.get(pass1Name);
      const pass2Control = formGroup.get(pass2Name);

      if(pass1Control?.value === pass2Control?.value){
        pass2Control?.setErrors(null);
      }else{
        pass2Control?.setErrors({noEsIgual:false})
      }
        
      
    }
  }
}
