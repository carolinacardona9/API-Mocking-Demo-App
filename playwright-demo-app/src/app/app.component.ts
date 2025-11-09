import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="container">
      <header>
        <div class="page-header">
          <img width="100" height="100" src="images/QA HIVELAB ICON.jpg" alt="" />
          <h1>Demo Playwright Mocking</h1>
        </div>
        <nav>
          <a routerLink="/users" routerLinkActive="active">Users</a>
          <a routerLink="/products" routerLinkActive="active">Products</a>
          <a routerLink="/images" routerLinkActive="active">Images</a>
        </nav>
      </header>
      <main>
        <router-outlet />
      </main>
    </div>
  `,
  styles: [
    `
      .page-header{
        display: flex;
        align-items: center;
        margin-bottom: 30px;
      }
      .container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 20px;
      }
      header {
        margin-bottom: 30px;
      }
      h1 {
        color: #333;
        margin-bottom: 20px;
      }
      nav {
        display: flex;
        gap: 10px;
        border-bottom: 2px solid #ddd;
        padding-bottom: 10px;
      }
      nav a {
        padding: 10px 20px;
        text-decoration: none;
        color: #666;
        border-radius: 4px 4px 0 0;
        transition: all 0.3s;
      }
      nav a:hover {
        background-color: #f0f0f0;
        color: #5f5dd1;
      }
      nav a.active {
        background-color: #5f5dd1;
        color: white;
      }
    `,
  ],
})
export class AppComponent {}
