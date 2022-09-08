import { Component, OnDestroy, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  name = 'oliver';
  counter = 0;
  people = [
    {name: 'oliver', age: 46},
    {name: 'marcia', age: 21},
    {name: 'sabrina', age: 18},
  ];
  mycolor = 'purple';

  ngOnInit(): void {
    this.counter = 2;
  }

  btnClick = (): void => {
    this.counter++;
    this.mycolor = 'red';
  }
}
