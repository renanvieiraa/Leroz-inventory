import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component, createPlatform, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';
import { Users } from '../models/users';
import { UsersService } from '../services/users.service';

@Component({
  selector: 'app-login-page',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {


  

  form:any;
  

  emailDB:string = "email@teste.com";
  senhaDB:string = "12345678";
  mensagem:string = "";

  constructor(private formBuilder:FormBuilder, private usersService:UsersService) {


    

    this.criarForm();
    
    
  }

  httpOptions = {
    headers: new HttpHeaders({'Content-Type': 'application/json'})
  }



  criarForm(){
    this.form = this.formBuilder.group({

      email: [''],
      senha: ['']
    })
  }


  login()
  {
    this.usersService.getUsers(this.form.get('email').value).then((users:Users[])=>{
      console.log('RETORNO',users)
      if(this.form.get('email').value == users[0].email && this.form.get('senha').value == users[0].password){
        this.mensagem = "Login feito com sucesso!";
      }else{
        this.mensagem = "E-mail ou a senha está errado!";
      }
    })
  }

  ngOnInit(): void {
    // console.log(this.usersService.getUsers())
  }

}
