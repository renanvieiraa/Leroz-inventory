import { Component, createPlatform, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

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

  constructor(private formBuilder:FormBuilder) {

    this.criarForm();
    
    
  }


  criarForm(){
    this.form = this.formBuilder.group({

      email: [''],
      senha: ['']
    })
  }


  login()
  {
    if(this.form.get('email').value == this.emailDB && this.form.get('senha').value == this.senhaDB){
      this.mensagem = "Login feito com sucesso!";
    }else{
      this.mensagem = "E-mail ou a senha está errado!";
    }

    
  }

  ngOnInit(): void {
  }

}
