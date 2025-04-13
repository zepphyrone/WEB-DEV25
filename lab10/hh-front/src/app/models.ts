export interface Company{
  "id":number,
  "name":string,
  "description":string,
  "city":string,
  "address":string
}
export interface Vacancy{
  "id":number,
  "name":string,
  "description":string,
  "salary":number,
  "Company":Company,
}
export interface Token{
  access:string,
  refresh:string,
}
