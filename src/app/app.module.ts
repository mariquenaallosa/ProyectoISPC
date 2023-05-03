import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';


// Componentes 
import { AdminComponent } from './pages/admin/admin.component';
import { AboutComponent } from './shared/about/about.component';

@NgModule({
  declarations: [
    AppComponent,
    AdminComponent,
    AboutComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]

})
export class AppModule { }
