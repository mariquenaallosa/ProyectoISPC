import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { FiltroDeBusquedaComponent } from './filtro-de-busqueda/filtro-de-busqueda.component';

@NgModule({
  declarations: [
    AppComponent,
    FiltroDeBusquedaComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
