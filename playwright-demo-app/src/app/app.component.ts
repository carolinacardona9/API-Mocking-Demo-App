import { Component } from '@angular/core';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="container">
      <header>
        <h1>Demo AG-Grid - Playwright Mocking</h1>
        <nav>
          <a routerLink="/users" routerLinkActive="active">Users</a>
          <a routerLink="/products" routerLinkActive="active">Products</a>
        </nav>
      </header>
      <main>
        <router-outlet />
      </main>
    </div>
  `,
  styles: [`
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
    }
    nav a.active {
      background-color: #007bff;
      color: white;
    }
  `]
})
export class AppComponent {}