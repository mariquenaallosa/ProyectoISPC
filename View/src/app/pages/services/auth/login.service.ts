import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { LoginRequest } from './loginRequest';
import { User } from './user';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }

  login(credentials:LoginRequest):Observable<User>{
    return this.http.get<User>('./assets/data.json');
  }
}
