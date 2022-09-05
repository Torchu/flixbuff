import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-review-create',
  templateUrl: './review-create.component.html',
  styleUrls: ['./review-create.component.scss']
})
export class ReviewCreateComponent {
  constructor(public dialogRef: MatDialogRef<ReviewCreateComponent>) {}

  /**
   * Closes the dialog
   */
  public close(): void {
    this.dialogRef.close(false);
  }
}
