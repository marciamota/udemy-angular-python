import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class PeopleService {
  people = [
    {name: 'oliver', age: 46},
    {name: 'marcia', age: 21},
    {name: 'sabrina', age: 18},
  ];

  constructor() { }

  allPeople() {
    return this.people;
  }
}
