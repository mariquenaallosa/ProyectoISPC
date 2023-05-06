import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CarrucelDestComponent } from './carrucel-dest/carrucel-dest.component';
import { AboutComponent } from './about/about.component';
import { BannerCarouselComponent } from './banner-carousel/banner-carousel.component';
import { FormContactComponent } from './form-contact/form-contact.component';



@NgModule({
  declarations: [
    CarrucelDestComponent,
    AboutComponent,
    BannerCarouselComponent,
    FormContactComponent
  ],
  exports:[
    CarrucelDestComponent,
    AboutComponent,
    BannerCarouselComponent,
    FormContactComponent
  ],
  imports: [
    CommonModule
  ]
})
export class SharedModule { }
