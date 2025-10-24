import { ChangeDetectionStrategy, Component } from '@angular/core';

@Component({
  selector: 'app-images-grid',
  imports: [],
  templateUrl: './images-grid.component.html',
  styleUrl: './images-grid.component.css',
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ImagesGridComponent { 
  uploadedFile: File | null = null
  previewUrl: string | null | ArrayBuffer = null
  handleFileUploaded($event: Event) {
    const input = $event.target as HTMLInputElement
    if (input.files && input.files.length > 0) {
      this.uploadedFile = input.files[0]
      const reader = new FileReader()
      reader.onload = () => {
        this.previewUrl = reader.result
      }
      reader.readAsDataURL(this.uploadedFile)
    } 
  }
}
