import { NgModule } from '@angular/core';
import { FooterComponent } from './footer/footer.component';
import { NavComponent } from './nav/nav.component';



@NgModule({
  declarations: [
    FooterComponent,
    NavComponent
  ],
  exports:[
    FooterComponent,
    NavComponent
  ],
  imports: [
    CommonModule
  ]
})
export class CommonModule { }
