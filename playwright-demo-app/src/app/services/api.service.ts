import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface User {
  id: number;
  name: string;
  email: string;
  role: string;
  status: string;
  createdAt: string;
}

export interface Product {
  id: number;
  name: string;
  category: string;
  price: number;
  stock: number;
  supplier: string;
}

export interface GridResponse<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getUsers(page: number = 1, pageSize: number = 10): Observable<GridResponse<User>> {
    return this.http.get<GridResponse<User>>(`${this.baseUrl}/users?page=${page}&pageSize=${pageSize}`);
  }

  getProducts(page: number = 1, pageSize: number = 10): Observable<GridResponse<Product>> {
    return this.http.get<GridResponse<Product>>(`${this.baseUrl}/products?page=${page}&pageSize=${pageSize}`);
  }
}