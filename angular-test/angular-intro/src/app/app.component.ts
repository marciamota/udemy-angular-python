import { Component, OnInit } from '@angular/core';
import { PeopleService } from './people.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  name = 'oliver';
  counter = 0;
  people: any[] = [];
  mycolor = 'purple';
  today = new Date();
  cash = 2;

  constructor(private peopleService: PeopleService) {

  }

  ngOnInit(): void {
    this.counter = 2;
    this.people = this.peopleService.allPeople();
  }

  btnClick = (): void => {
    this.counter++;
    this.mycolor = 'red';
  }
}
