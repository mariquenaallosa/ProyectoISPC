import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarrucelDestComponent } from './carrucel-dest/carrucel-dest.component';
import { AboutComponent } from './about/about.component';



@NgModule({
  declarations: [
    CarrucelDestComponent,
    AboutComponent
  ],
  imports: [
    CommonModule
  ]
})
export class SharedModule { }
