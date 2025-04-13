import {Component, OnInit} from '@angular/core';
import {RouterModule, RouterOutlet} from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AboutComponent} from "./about/about.component";
import {VacanciesComponent} from "./vacancies/vacancies.component";
import {CompaniesComponent} from "./companies/companies.component";
import {NotFoundComponent} from "./not-found/not-found.component";
import {CommonModule} from "@angular/common";
import {FormsModule} from "@angular/forms";
import {HHService} from "./hh.service";



@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule, HomeComponent, AboutComponent, VacanciesComponent, CompaniesComponent, VacanciesComponent, NotFoundComponent, RouterOutlet, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit{
  constructor(private hhService:HHService) {
  }

  ngOnInit(): void {
    
    }
    logged:boolean=false;
    title = 'hh-front';
    username :string='';
    password:string='';
  login(){
    return this.hhService.login(this.username,this.password).subscribe(data=>{
      this.logged=true;
      localStorage.setItem("access",data.access)
      localStorage.setItem("refresh",data.refresh)

    })

  }
  logout(){
    this.logged=false;
    localStorage.removeItem("access")
    localStorage.removeItem("refresh")

  }


}
