import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AgGridAngular } from 'ag-grid-angular';
import { ColDef, GridApi, GridReadyEvent } from 'ag-grid-community';
import { ApiService, User } from '../../services/api.service';

@Component({
  selector: 'app-users-grid',
  imports: [CommonModule, FormsModule, AgGridAngular],
  template: `
    <div class="grid-container">
      <h2>Users Grid</h2>
      <div class="info-bar">
        <span>Total Records: {{ totalRecords }}</span>
        <span>Current Page: {{ currentPage }}</span>
        <span>Page Size: {{ pageSize }}</span>
      </div>
      <ag-grid-angular
        class="ag-theme-alpine"
        [columnDefs]="columnDefs"
        [rowData]="rowData"
        [pagination]="true"
        [paginationPageSize]="pageSize"
        [paginationPageSizeSelector]="[10, 25, 50, 100]"
        [suppressPaginationPanel]="false"
        (gridReady)="onGridReady($event)"
        style="width: 100%; height: 600px;"
      />
      <div class="pagination-controls">
        <button (click)="previousPage()" [disabled]="currentPage === 1">Previous</button>
        <span>Page {{ currentPage }} of {{ totalPages }}</span>
        <button (click)="nextPage()" [disabled]="currentPage >= totalPages">Next</button>
        <select [(ngModel)]="pageSize" (change)="onPageSizeChange()">
          <option [value]="10">10</option>
          <option [value]="25">25</option>
          <option [value]="50">50</option>
          <option [value]="100">100</option>
        </select>
      </div>
    </div>
  `,
  styles: [`
    .grid-container {
      padding: 20px;
    }
    h2 {
      margin-bottom: 20px;
      color: #333;
    }
    .info-bar {
      display: flex;
      gap: 20px;
      margin-bottom: 15px;
      padding: 10px;
      background-color: #f8f9fa;
      border-radius: 4px;
    }
    .info-bar span {
      font-weight: 500;
      color: #666;
    }
    .pagination-controls {
      margin-top: 15px;
      display: flex;
      align-items: center;
      gap: 15px;
      padding: 10px;
      background-color: #f8f9fa;
      border-radius: 4px;
    }
    .pagination-controls button {
      padding: 8px 16px;
      background-color: #007bff;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    .pagination-controls button:disabled {
      background-color: #ccc;
      cursor: not-allowed;
    }
    .pagination-controls select {
      padding: 8px;
      border-radius: 4px;
      border: 1px solid #ddd;
    }
  `]
})
export class UsersGridComponent implements OnInit {
  private gridApi!: GridApi;
  rowData: User[] = [];
  totalRecords = 0;
  currentPage = 1;
  pageSize = 10;

  get totalPages(): number {
    return Math.ceil(this.totalRecords / this.pageSize);
  }

  columnDefs: ColDef[] = [
    { field: 'id', headerName: 'ID', width: 80 },
    { field: 'name', headerName: 'Name', width: 200, flex: 1 },
    { field: 'email', headerName: 'Email', width: 250, flex: 1 },
    { field: 'role', headerName: 'Role', width: 150 },
    { 
      field: 'status', 
      headerName: 'Status', 
      width: 120,
      cellStyle: (params: any) => {
        if (params.value === 'Active') return { color: 'green', fontWeight: 'bold' };
        if (params.value === 'Inactive') return { color: 'red', fontWeight: 'normal' };
        return { color: 'orange', fontWeight: 'normal' };
      }
    },
    { field: 'createdAt', headerName: 'Created At', width: 180 }
  ];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadData();
  }

  onGridReady(params: GridReadyEvent) {
    this.gridApi = params.api;
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.currentPage--;
      this.loadData();
    }
  }

  nextPage() {
    if (this.currentPage < this.totalPages) {
      this.currentPage++;
      this.loadData();
    }
  }

  onPageSizeChange() {
    this.currentPage = 1; // Reset to first page
    this.loadData();
  }

  loadData() {
    this.apiService.getUsers(this.currentPage, this.pageSize).subscribe({
      next: (response) => {
        this.rowData = response.data;
        this.totalRecords = response.total;
      },
      error: (error) => {
        console.error('Error loading users:', error);
      }
    });
  }
}