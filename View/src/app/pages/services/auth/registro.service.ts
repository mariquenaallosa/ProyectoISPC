import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RegistroRequest } from './registroRequest';
import { UserRegistro } from './userRegistro';

@Injectable({
  providedIn: 'root'
})
export class RegistroService {

  constructor(private http: HttpClient) { }

  registro(credentials:RegistroRequest):Observable<UserRegistro>{
    return this.http.get<UserRegistro>('./assets/data.json');
  }
}
