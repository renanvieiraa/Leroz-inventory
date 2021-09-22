import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Users } from '../models/users';

@Injectable({
  providedIn: 'root'
})
export class UsersService {

  baseDB = 'http://127.0.0.1:5000/';

  constructor(private httpClient:HttpClient) { }

  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type':'application/json'})
  }

  getUsers(usuario:string):Promise<Users[]>{
    return this.httpClient.get<Users>(this.baseDB+'users'+'/'+usuario, this.httpOptions)
      .toPromise()
        .then((users:Users)=>{
          return users;
        })
        .catch((error)=>{
          return error
        })
  }

}
