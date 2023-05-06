import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';



@NgModule({
  declarations: [
    AdminComponent,
    LoginComponent,
    HomeComponent
  ],
  exports: [
    HomeComponent,
    LoginComponent,
    AdminComponent
  ],
  imports: [
    CommonModule
  ]
})
export class PagesModule { }
