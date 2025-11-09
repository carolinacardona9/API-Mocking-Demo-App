import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

interface ImageData {
  url: string;
  title: string;
  loaded: boolean;
  error: boolean;
}

@Component({
  selector: 'app-images-grid',
  imports: [CommonModule],
  templateUrl: './images-grid.component.html',
  styleUrl: './images-grid.component.css',
})
export class ImagesGridComponent implements OnInit {
  images: ImageData[] = [
    {
      url: 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&h=600&fit=crop',
      title: 'Laptop',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=600&fit=crop',
      title: 'Smartphone',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=600&fit=crop',
      title: 'Auriculares',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=800&h=600&fit=crop',
      title: 'Smartwatch',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=800&h=600&fit=crop',
      title: 'Tablet',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=800&h=600&fit=crop',
      title: 'Teclado',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800&h=600&fit=crop',
      title: 'Mouse',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=800&h=600&fit=crop',
      title: 'Monitor',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1606983340126-99ab4feaa64a?w=800&h=600&fit=crop',
      title: 'Cámara',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800&h=600&fit=crop',
      title: 'Auriculares Gaming',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&h=600&fit=crop',
      title: 'iPad',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1434493789847-2f02dc6ca35d?w=800&h=600&fit=crop',
      title: 'Reloj Inteligente',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=800&h=600&fit=crop',
      title: 'MacBook',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800&h=600&fit=crop&auto=format',
      title: 'iPhone',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&h=600&fit=crop',
      title: 'Teclado RGB',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1527814050087-3793815479db?w=800&h=600&fit=crop',
      title: 'Mouse Gaming',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1593642632823-8f785ba67e45?w=800&h=600&fit=crop',
      title: 'Monitor Curvo',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1606983340126-99ab4feaa64a?w=800&h=600&fit=crop&auto=format',
      title: 'Cámara DSLR',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=800&h=600&fit=crop&auto=format',
      title: 'Altavoz Bluetooth',
      loaded: false,
      error: false
    },
    {
      url: 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=800&h=600&fit=crop',
      title: 'Zapatillas',
      loaded: false,
      error: false
    }
  ];

  ngOnInit() {
    // Las imágenes se cargarán automáticamente cuando se rendericen en el template
    // Esto permite que Playwright intercepte las peticiones HTTP
  }

  onImageLoad(index: number) {
    this.images[index].loaded = true;
    this.images[index].error = false;
  }

  onImageError(index: number) {
    this.images[index].loaded = false;
    this.images[index].error = true;
  }
}
