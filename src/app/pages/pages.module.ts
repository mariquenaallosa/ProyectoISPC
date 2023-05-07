import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AdminComponent } from './admin/admin.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { GaleriaComponent } from './galeria/galeria.component';
import { UsersComponent } from './users/users.component';



@NgModule({
  declarations: [
    HomeComponent,
    AdminComponent,
    LoginComponent,
    GaleriaComponent,
    UsersComponent
  ],
  exports: [
    HomeComponent,
    AdminComponent,
    LoginComponent,
    GaleriaComponent,
    UsersComponent
  ],
  imports: [
    CommonModule
  ]
})
export class PagesModule { }
