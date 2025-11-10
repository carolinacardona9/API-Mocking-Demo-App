import { Routes } from '@angular/router';
import { UsersGridComponent } from './components/users-grid/users-grid.component';
import { ProductsGridComponent } from './components/products-grid/products-grid.component';
import { ImagesGridComponent } from './components/images-grid/images-grid.component';

export const routes: Routes = [
  { path: '', redirectTo: 'users', pathMatch: 'full' },
  { path: 'users', component: UsersGridComponent },
  { path: 'products', component: ProductsGridComponent },
  { path: 'images', component: ImagesGridComponent }
];