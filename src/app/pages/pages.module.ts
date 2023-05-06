import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';



@NgModule({
  declarations: [
    AdminComponent,
    LoginComponent
  ],
  exports: [
    LoginComponent,
    AdminComponent
  ],
  imports: [
    CommonModule
  ]
})
export class PagesModule { }
