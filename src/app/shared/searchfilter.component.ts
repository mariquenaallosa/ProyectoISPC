import { Component, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-filtro-de-busqueda',
  templateUrl: './filtro-de-busqueda.component.html',
  styleUrls: ['./filtro-de-busqueda.component.css']
})
export class FiltroDeBusquedaComponent {
  filtro: string = '';

  @Output() buscar: EventEmitter<string> = new EventEmitter<string>();

  handleFiltroChange(event: Event): void {
    this.filtro = (<HTMLInputElement>event.target).value;
  }

  handleBuscarClick(): void {
    this.buscar.emit(this.filtro);
  }
}
