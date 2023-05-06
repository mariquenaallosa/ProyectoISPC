import { AppRoutingModule } from './app-routing.module';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { CommonModule } from '@angular/common';
import { PagesModule } from './pages/pages.module';
import { NavComponent } from './common/nav/nav.component';
import { FooterComponent } from './common/footer/footer.component';


@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    FooterComponent
  ],
  imports: [
    AppRoutingModule,
    BrowserModule,
    CommonModule,
    PagesModule
  ],
  providers: [],
  bootstrap: [AppComponent]

})
export class AppModule { }
