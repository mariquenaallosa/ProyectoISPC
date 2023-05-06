import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarrucelDestComponent } from './carrucel-dest/carrucel-dest.component';
import { AboutComponent } from './about/about.component';
import { BannerCarouselComponent } from './banner-carousel/banner-carousel.component';



@NgModule({
  declarations: [
    CarrucelDestComponent,
    AboutComponent,
    BannerCarouselComponent
  ],
  imports: [
    CommonModule
  ]
})
export class SharedModule { }
