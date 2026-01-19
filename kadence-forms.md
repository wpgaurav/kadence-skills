# Kadence Advanced Forms Skill

**Activation**: Creating contact forms, newsletter signups, registration forms, surveys, quote requests with Kadence Blocks.

## Form Block Structure

Kadence Advanced Form uses a parent-child structure:
- `kadence/advanced-form` - Container with form settings (saved as post type)
- Field blocks placed directly inside or within `kadence/column` for multi-column layouts
- `kadence/advanced-form-submit` - Submit button (required)

## Available Field Types

| Block | Use Case |
|-------|----------|
| `kadence/advanced-form-text` | Single-line text input |
| `kadence/advanced-form-email` | Email address input |
| `kadence/advanced-form-textarea` | Multi-line text area |
| `kadence/advanced-form-telephone` | Phone number input |
| `kadence/advanced-form-number` | Numeric input |
| `kadence/advanced-form-select` | Dropdown selection |
| `kadence/advanced-form-radio` | Radio button group |
| `kadence/advanced-form-checkbox` | Checkbox group |
| `kadence/advanced-form-date` | Date picker |
| `kadence/advanced-form-time` | Time picker |
| `kadence/advanced-form-file` | File upload |
| `kadence/advanced-form-accept` | Terms acceptance checkbox |
| `kadence/advanced-form-hidden` | Hidden field |
| `kadence/advanced-form-captcha` | CAPTCHA protection |
| `kadence/advanced-form-submit` | Submit button |

## Form Patterns

### Pattern 1: Simple Contact Form

Basic contact form with name, email, and message.

```html
<!-- wp:kadence/advanced-form {"id":1,"uniqueID":"kt-form-001"} -->
<div class="wp-block-kadence-advanced-form kb-advanced-form-kt-form-001">

<!-- wp:kadence/advanced-form-text {"uniqueID":"kt-field-001","label":"Your Name","placeholder":"Enter your name","required":true,"inputName":"name"} -->
<div class="kb-adv-form-field kb-adv-form-text-field kb-field-kt-field-001"><label for="kb-field-kt-field-001">Your Name<span class="required">*</span></label><input type="text" name="name" id="kb-field-kt-field-001" placeholder="Enter your name" required /></div>
<!-- /wp:kadence/advanced-form-text -->

<!-- wp:kadence/advanced-form-email {"uniqueID":"kt-field-002","label":"Email Address","placeholder":"you@example.com","required":true,"inputName":"email"} -->
<div class="kb-adv-form-field kb-adv-form-email-field kb-field-kt-field-002"><label for="kb-field-kt-field-002">Email Address<span class="required">*</span></label><input type="email" name="email" id="kb-field-kt-field-002" placeholder="you@example.com" required /></div>
<!-- /wp:kadence/advanced-form-email -->

<!-- wp:kadence/advanced-form-textarea {"uniqueID":"kt-field-003","label":"Message","placeholder":"How can we help you?","required":true,"rows":5,"inputName":"message"} -->
<div class="kb-adv-form-field kb-adv-form-textarea-field kb-field-kt-field-003"><label for="kb-field-kt-field-003">Message<span class="required">*</span></label><textarea name="message" id="kb-field-kt-field-003" placeholder="How can we help you?" rows="5" required></textarea></div>
<!-- /wp:kadence/advanced-form-textarea -->

<!-- wp:kadence/advanced-form-submit {"uniqueID":"kt-submit-001","text":"Send Message","sizePreset":"large","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"hAlign":"left"} -->
<div class="kb-adv-form-field kb-submit-field kb-field-kt-submit-001"><button type="submit" class="kb-adv-form-submit-btn">Send Message</button></div>
<!-- /wp:kadence/advanced-form-submit -->

</div>
<!-- /wp:kadence/advanced-form -->
```

### Pattern 2: Two-Column Contact Form

Contact form with side-by-side fields using rowlayout.

```html
<!-- wp:kadence/advanced-form {"id":2,"uniqueID":"kt-form-002"} -->
<div class="wp-block-kadence-advanced-form kb-advanced-form-kt-form-002">

<!-- wp:kadence/rowlayout {"uniqueID":"kt-form-row-001","columns":2,"colLayout":"equal","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-form-row-001">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-default">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-form-col-001a"} -->
<div class="wp-block-kadence-column kadence-column-form-col-001a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-text {"uniqueID":"kt-field-f001","label":"First Name","placeholder":"First name","required":true,"inputName":"first_name"} -->
<div class="kb-adv-form-field kb-adv-form-text-field kb-field-kt-field-f001"><label for="kb-field-kt-field-f001">First Name<span class="required">*</span></label><input type="text" name="first_name" id="kb-field-kt-field-f001" placeholder="First name" required /></div>
<!-- /wp:kadence/advanced-form-text -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-form-col-001b"} -->
<div class="wp-block-kadence-column kadence-column-form-col-001b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-text {"uniqueID":"kt-field-f002","label":"Last Name","placeholder":"Last name","required":true,"inputName":"last_name"} -->
<div class="kb-adv-form-field kb-adv-form-text-field kb-field-kt-field-f002"><label for="kb-field-kt-field-f002">Last Name<span class="required">*</span></label><input type="text" name="last_name" id="kb-field-kt-field-f002" placeholder="Last name" required /></div>
<!-- /wp:kadence/advanced-form-text -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- wp:kadence/rowlayout {"uniqueID":"kt-form-row-002","columns":2,"colLayout":"equal","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-form-row-002">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-default">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-form-col-002a"} -->
<div class="wp-block-kadence-column kadence-column-form-col-002a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-email {"uniqueID":"kt-field-f003","label":"Email","placeholder":"you@example.com","required":true,"inputName":"email"} -->
<div class="kb-adv-form-field kb-adv-form-email-field kb-field-kt-field-f003"><label for="kb-field-kt-field-f003">Email<span class="required">*</span></label><input type="email" name="email" id="kb-field-kt-field-f003" placeholder="you@example.com" required /></div>
<!-- /wp:kadence/advanced-form-email -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-form-col-002b"} -->
<div class="wp-block-kadence-column kadence-column-form-col-002b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-telephone {"uniqueID":"kt-field-f004","label":"Phone","placeholder":"+1 (555) 000-0000","inputName":"phone"} -->
<div class="kb-adv-form-field kb-adv-form-tel-field kb-field-kt-field-f004"><label for="kb-field-kt-field-f004">Phone</label><input type="tel" name="phone" id="kb-field-kt-field-f004" placeholder="+1 (555) 000-0000" /></div>
<!-- /wp:kadence/advanced-form-telephone -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- wp:kadence/advanced-form-select {"uniqueID":"kt-field-f005","label":"How did you hear about us?","inputName":"source","options":[{"value":"google","label":"Google Search"},{"value":"social","label":"Social Media"},{"value":"referral","label":"Referral"},{"value":"other","label":"Other"}]} -->
<div class="kb-adv-form-field kb-adv-form-select-field kb-field-kt-field-f005"><label for="kb-field-kt-field-f005">How did you hear about us?</label><select name="source" id="kb-field-kt-field-f005"><option value="google">Google Search</option><option value="social">Social Media</option><option value="referral">Referral</option><option value="other">Other</option></select></div>
<!-- /wp:kadence/advanced-form-select -->

<!-- wp:kadence/advanced-form-textarea {"uniqueID":"kt-field-f006","label":"Your Message","placeholder":"Tell us about your project...","required":true,"rows":4,"inputName":"message"} -->
<div class="kb-adv-form-field kb-adv-form-textarea-field kb-field-kt-field-f006"><label for="kb-field-kt-field-f006">Your Message<span class="required">*</span></label><textarea name="message" id="kb-field-kt-field-f006" placeholder="Tell us about your project..." rows="4" required></textarea></div>
<!-- /wp:kadence/advanced-form-textarea -->

<!-- wp:kadence/advanced-form-submit {"uniqueID":"kt-submit-002","text":"Submit Request","sizePreset":"large","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"hAlign":"left","widthType":"full"} -->
<div class="kb-adv-form-field kb-submit-field kb-field-kt-submit-002"><button type="submit" class="kb-adv-form-submit-btn">Submit Request</button></div>
<!-- /wp:kadence/advanced-form-submit -->

</div>
<!-- /wp:kadence/advanced-form -->
```

### Pattern 3: Newsletter Signup Form

Compact inline newsletter subscription.

```html
<!-- wp:kadence/advanced-form {"id":3,"uniqueID":"kt-form-003"} -->
<div class="wp-block-kadence-advanced-form kb-advanced-form-kt-form-003">

<!-- wp:kadence/rowlayout {"uniqueID":"kt-form-row-nl","columns":2,"colLayout":"right-forty","columnGutter":"narrow","verticalAlignment":"bottom"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-form-row-nl">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-narrow kt-row-valign-bottom">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-form-col-nl-a"} -->
<div class="wp-block-kadence-column kadence-column-form-col-nl-a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-email {"uniqueID":"kt-field-nl001","label":"Email Address","showLabel":false,"placeholder":"Enter your email address","required":true,"inputName":"email"} -->
<div class="kb-adv-form-field kb-adv-form-email-field kb-field-kt-field-nl001"><input type="email" name="email" id="kb-field-kt-field-nl001" placeholder="Enter your email address" required /></div>
<!-- /wp:kadence/advanced-form-email -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-form-col-nl-b"} -->
<div class="wp-block-kadence-column kadence-column-form-col-nl-b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-submit {"uniqueID":"kt-submit-nl","text":"Subscribe","sizePreset":"medium","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"widthType":"full","icon":"fe_mail","iconSide":"left"} -->
<div class="kb-adv-form-field kb-submit-field kb-field-kt-submit-nl"><button type="submit" class="kb-adv-form-submit-btn"><span class="kt-btn-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></span>Subscribe</button></div>
<!-- /wp:kadence/advanced-form-submit -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

</div>
<!-- /wp:kadence/advanced-form -->
```

### Pattern 4: Quote Request Form

Detailed form with multiple field types.

```html
<!-- wp:kadence/advanced-form {"id":4,"uniqueID":"kt-form-004"} -->
<div class="wp-block-kadence-advanced-form kb-advanced-form-kt-form-004">

<!-- wp:kadence/rowlayout {"uniqueID":"kt-form-row-q1","columns":2,"colLayout":"equal","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-form-row-q1">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-default">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-form-col-q1a"} -->
<div class="wp-block-kadence-column kadence-column-form-col-q1a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-text {"uniqueID":"kt-field-q001","label":"Full Name","required":true,"inputName":"name"} -->
<div class="kb-adv-form-field kb-adv-form-text-field kb-field-kt-field-q001"><label for="kb-field-kt-field-q001">Full Name<span class="required">*</span></label><input type="text" name="name" id="kb-field-kt-field-q001" required /></div>
<!-- /wp:kadence/advanced-form-text -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-form-col-q1b"} -->
<div class="wp-block-kadence-column kadence-column-form-col-q1b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-text {"uniqueID":"kt-field-q002","label":"Company Name","inputName":"company"} -->
<div class="kb-adv-form-field kb-adv-form-text-field kb-field-kt-field-q002"><label for="kb-field-kt-field-q002">Company Name</label><input type="text" name="company" id="kb-field-kt-field-q002" /></div>
<!-- /wp:kadence/advanced-form-text -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- wp:kadence/rowlayout {"uniqueID":"kt-form-row-q2","columns":2,"colLayout":"equal","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-form-row-q2">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-default">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-form-col-q2a"} -->
<div class="wp-block-kadence-column kadence-column-form-col-q2a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-email {"uniqueID":"kt-field-q003","label":"Email","required":true,"inputName":"email"} -->
<div class="kb-adv-form-field kb-adv-form-email-field kb-field-kt-field-q003"><label for="kb-field-kt-field-q003">Email<span class="required">*</span></label><input type="email" name="email" id="kb-field-kt-field-q003" required /></div>
<!-- /wp:kadence/advanced-form-email -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-form-col-q2b"} -->
<div class="wp-block-kadence-column kadence-column-form-col-q2b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-telephone {"uniqueID":"kt-field-q004","label":"Phone","inputName":"phone"} -->
<div class="kb-adv-form-field kb-adv-form-tel-field kb-field-kt-field-q004"><label for="kb-field-kt-field-q004">Phone</label><input type="tel" name="phone" id="kb-field-kt-field-q004" /></div>
<!-- /wp:kadence/advanced-form-telephone -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- wp:kadence/advanced-form-select {"uniqueID":"kt-field-q005","label":"Project Type","required":true,"inputName":"project_type","options":[{"value":"","label":"Select a project type..."},{"value":"website","label":"New Website"},{"value":"redesign","label":"Website Redesign"},{"value":"ecommerce","label":"E-commerce Store"},{"value":"webapp","label":"Web Application"},{"value":"other","label":"Other"}]} -->
<div class="kb-adv-form-field kb-adv-form-select-field kb-field-kt-field-q005"><label for="kb-field-kt-field-q005">Project Type<span class="required">*</span></label><select name="project_type" id="kb-field-kt-field-q005" required><option value="">Select a project type...</option><option value="website">New Website</option><option value="redesign">Website Redesign</option><option value="ecommerce">E-commerce Store</option><option value="webapp">Web Application</option><option value="other">Other</option></select></div>
<!-- /wp:kadence/advanced-form-select -->

<!-- wp:kadence/rowlayout {"uniqueID":"kt-form-row-q3","columns":2,"colLayout":"equal","columnGutter":"default"} -->
<div class="wp-block-kadence-rowlayout kt-row-layout-inner kt-layout-id-form-row-q3">
<div class="kt-row-column-wrap kt-has-2-columns kt-gutter-default">

<!-- wp:kadence/column {"id":1,"uniqueID":"kt-form-col-q3a"} -->
<div class="wp-block-kadence-column kadence-column-form-col-q3a"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-select {"uniqueID":"kt-field-q006","label":"Budget Range","inputName":"budget","options":[{"value":"","label":"Select budget range..."},{"value":"5k-10k","label":"$5,000 - $10,000"},{"value":"10k-25k","label":"$10,000 - $25,000"},{"value":"25k-50k","label":"$25,000 - $50,000"},{"value":"50k+","label":"$50,000+"}]} -->
<div class="kb-adv-form-field kb-adv-form-select-field kb-field-kt-field-q006"><label for="kb-field-kt-field-q006">Budget Range</label><select name="budget" id="kb-field-kt-field-q006"><option value="">Select budget range...</option><option value="5k-10k">$5,000 - $10,000</option><option value="10k-25k">$10,000 - $25,000</option><option value="25k-50k">$25,000 - $50,000</option><option value="50k+">$50,000+</option></select></div>
<!-- /wp:kadence/advanced-form-select -->

</div></div>
<!-- /wp:kadence/column -->

<!-- wp:kadence/column {"id":2,"uniqueID":"kt-form-col-q3b"} -->
<div class="wp-block-kadence-column kadence-column-form-col-q3b"><div class="kt-inside-inner-col">

<!-- wp:kadence/advanced-form-date {"uniqueID":"kt-field-q007","label":"Desired Start Date","inputName":"start_date"} -->
<div class="kb-adv-form-field kb-adv-form-date-field kb-field-kt-field-q007"><label for="kb-field-kt-field-q007">Desired Start Date</label><input type="date" name="start_date" id="kb-field-kt-field-q007" /></div>
<!-- /wp:kadence/advanced-form-date -->

</div></div>
<!-- /wp:kadence/column -->

</div>
</div>
<!-- /wp:kadence/rowlayout -->

<!-- wp:kadence/advanced-form-checkbox {"uniqueID":"kt-field-q008","label":"Services Needed","inputName":"services","options":[{"value":"design","label":"UI/UX Design","selected":false},{"value":"development","label":"Custom Development","selected":false},{"value":"seo","label":"SEO Optimization","selected":false},{"value":"hosting","label":"Managed Hosting","selected":false},{"value":"maintenance","label":"Ongoing Maintenance","selected":false}],"inline":true} -->
<div class="kb-adv-form-field kb-adv-form-checkbox-field kb-field-kt-field-q008"><label>Services Needed</label><div class="kb-checkbox-group"><label><input type="checkbox" name="services[]" value="design" /> UI/UX Design</label><label><input type="checkbox" name="services[]" value="development" /> Custom Development</label><label><input type="checkbox" name="services[]" value="seo" /> SEO Optimization</label><label><input type="checkbox" name="services[]" value="hosting" /> Managed Hosting</label><label><input type="checkbox" name="services[]" value="maintenance" /> Ongoing Maintenance</label></div></div>
<!-- /wp:kadence/advanced-form-checkbox -->

<!-- wp:kadence/advanced-form-textarea {"uniqueID":"kt-field-q009","label":"Project Details","placeholder":"Tell us about your project goals, requirements, and any other relevant information...","rows":6,"inputName":"details"} -->
<div class="kb-adv-form-field kb-adv-form-textarea-field kb-field-kt-field-q009"><label for="kb-field-kt-field-q009">Project Details</label><textarea name="details" id="kb-field-kt-field-q009" placeholder="Tell us about your project goals, requirements, and any other relevant information..." rows="6"></textarea></div>
<!-- /wp:kadence/advanced-form-textarea -->

<!-- wp:kadence/advanced-form-accept {"uniqueID":"kt-field-q010","label":"Terms","required":true,"description":"I agree to the <a href=\"/privacy-policy\">Privacy Policy</a> and <a href=\"/terms\">Terms of Service</a>","inputName":"terms"} -->
<div class="kb-adv-form-field kb-adv-form-accept-field kb-field-kt-field-q010"><label><input type="checkbox" name="terms" required /> I agree to the <a href="/privacy-policy">Privacy Policy</a> and <a href="/terms">Terms of Service</a><span class="required">*</span></label></div>
<!-- /wp:kadence/advanced-form-accept -->

<!-- wp:kadence/advanced-form-submit {"uniqueID":"kt-submit-q","text":"Request Quote","sizePreset":"large","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"hAlign":"left","icon":"fe_send","iconSide":"right"} -->
<div class="kb-adv-form-field kb-submit-field kb-field-kt-submit-q"><button type="submit" class="kb-adv-form-submit-btn">Request Quote<span class="kt-btn-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg></span></button></div>
<!-- /wp:kadence/advanced-form-submit -->

</div>
<!-- /wp:kadence/advanced-form -->
```

### Pattern 5: Feedback/Survey Form with Radio Buttons

Collect feedback with radio button choices.

```html
<!-- wp:kadence/advanced-form {"id":5,"uniqueID":"kt-form-005"} -->
<div class="wp-block-kadence-advanced-form kb-advanced-form-kt-form-005">

<!-- wp:kadence/advanced-form-radio {"uniqueID":"kt-field-fb001","label":"How satisfied are you with our service?","required":true,"inputName":"satisfaction","options":[{"value":"very_satisfied","label":"Very Satisfied","selected":false},{"value":"satisfied","label":"Satisfied","selected":false},{"value":"neutral","label":"Neutral","selected":false},{"value":"dissatisfied","label":"Dissatisfied","selected":false},{"value":"very_dissatisfied","label":"Very Dissatisfied","selected":false}]} -->
<div class="kb-adv-form-field kb-adv-form-radio-field kb-field-kt-field-fb001"><label>How satisfied are you with our service?<span class="required">*</span></label><div class="kb-radio-group"><label><input type="radio" name="satisfaction" value="very_satisfied" required /> Very Satisfied</label><label><input type="radio" name="satisfaction" value="satisfied" /> Satisfied</label><label><input type="radio" name="satisfaction" value="neutral" /> Neutral</label><label><input type="radio" name="satisfaction" value="dissatisfied" /> Dissatisfied</label><label><input type="radio" name="satisfaction" value="very_dissatisfied" /> Very Dissatisfied</label></div></div>
<!-- /wp:kadence/advanced-form-radio -->

<!-- wp:kadence/advanced-form-radio {"uniqueID":"kt-field-fb002","label":"Would you recommend us to others?","required":true,"inputName":"recommend","options":[{"value":"definitely","label":"Definitely yes","selected":false},{"value":"probably","label":"Probably yes","selected":false},{"value":"not_sure","label":"Not sure","selected":false},{"value":"probably_not","label":"Probably not","selected":false},{"value":"definitely_not","label":"Definitely not","selected":false}],"inline":true} -->
<div class="kb-adv-form-field kb-adv-form-radio-field kb-field-kt-field-fb002"><label>Would you recommend us to others?<span class="required">*</span></label><div class="kb-radio-group kb-radio-inline"><label><input type="radio" name="recommend" value="definitely" required /> Definitely yes</label><label><input type="radio" name="recommend" value="probably" /> Probably yes</label><label><input type="radio" name="recommend" value="not_sure" /> Not sure</label><label><input type="radio" name="recommend" value="probably_not" /> Probably not</label><label><input type="radio" name="recommend" value="definitely_not" /> Definitely not</label></div></div>
<!-- /wp:kadence/advanced-form-radio -->

<!-- wp:kadence/advanced-form-textarea {"uniqueID":"kt-field-fb003","label":"What could we do better?","placeholder":"Your feedback helps us improve...","rows":4,"inputName":"feedback"} -->
<div class="kb-adv-form-field kb-adv-form-textarea-field kb-field-kt-field-fb003"><label for="kb-field-kt-field-fb003">What could we do better?</label><textarea name="feedback" id="kb-field-kt-field-fb003" placeholder="Your feedback helps us improve..." rows="4"></textarea></div>
<!-- /wp:kadence/advanced-form-textarea -->

<!-- wp:kadence/advanced-form-email {"uniqueID":"kt-field-fb004","label":"Email (optional)","placeholder":"your@email.com","helpText":"Only if you'd like us to follow up","inputName":"email"} -->
<div class="kb-adv-form-field kb-adv-form-email-field kb-field-kt-field-fb004"><label for="kb-field-kt-field-fb004">Email (optional)</label><input type="email" name="email" id="kb-field-kt-field-fb004" placeholder="your@email.com" /><p class="kb-field-help">Only if you'd like us to follow up</p></div>
<!-- /wp:kadence/advanced-form-email -->

<!-- wp:kadence/advanced-form-submit {"uniqueID":"kt-submit-fb","text":"Submit Feedback","sizePreset":"large","color":"#ffffff","background":"palette1","backgroundHover":"palette2","borderRadius":[6,6,6,6],"hAlign":"center","widthType":"full"} -->
<div class="kb-adv-form-field kb-submit-field kb-field-kt-submit-fb"><button type="submit" class="kb-adv-form-submit-btn">Submit Feedback</button></div>
<!-- /wp:kadence/advanced-form-submit -->

</div>
<!-- /wp:kadence/advanced-form -->
```

## Field Attribute Reference

### Common Field Attributes

All field types share these attributes:

```json
{
  "uniqueID": "kt-field-xxx",
  "formID": "kt-form-xxx",
  "label": "Field Label",
  "showLabel": true,
  "placeholder": "Placeholder text",
  "required": false,
  "defaultValue": "",
  "helpText": "Helper text below field",
  "inputName": "field_name",
  "ariaDescription": "",
  "maxWidth": ["100","",""],
  "maxWidthUnit": "%",
  "errorMessage": "Custom error",
  "requiredMessage": "This field is required"
}
```

### Select/Radio/Checkbox Options

```json
{
  "options": [
    {"value": "option1", "label": "Option 1", "selected": false},
    {"value": "option2", "label": "Option 2", "selected": false},
    {"value": "option3", "label": "Option 3", "selected": true}
  ],
  "inline": false,
  "multiSelect": false
}
```

### Submit Button Attributes

```json
{
  "uniqueID": "kt-submit-xxx",
  "text": "Submit",
  "sizePreset": "large",
  "style": "basic",
  "color": "#ffffff",
  "background": "palette1",
  "backgroundHover": "palette2",
  "borderRadius": [6,6,6,6],
  "hAlign": "left",
  "thAlign": "",
  "mhAlign": "",
  "widthType": "auto",
  "icon": "",
  "iconSide": "right"
}
```

## Size Presets

| Preset | Use Case |
|--------|----------|
| `small` | Compact forms, sidebars |
| `standard` | Default size |
| `medium` | Slightly larger |
| `large` | Prominent buttons |
| `xlarge` | Hero CTAs |

## Layout Tips

### Multi-Column Forms

Use `kadence/rowlayout` and `kadence/column` inside forms:

```html
<!-- wp:kadence/rowlayout {"columns":2,"colLayout":"equal"} -->
  <!-- wp:kadence/column -->
    <!-- Field 1 -->
  <!-- /wp:kadence/column -->
  <!-- wp:kadence/column -->
    <!-- Field 2 -->
  <!-- /wp:kadence/column -->
<!-- /wp:kadence/rowlayout -->
```

### Width Options

| `widthType` | Behavior |
|-------------|----------|
| `auto` | Natural button width |
| `fixed` | Set specific width |
| `full` | 100% container width |

## Best Practices

1. **Required fields**: Mark essential fields as required
2. **Labels**: Always show labels for accessibility
3. **Placeholders**: Use as hints, not replacements for labels
4. **Help text**: Explain complex fields
5. **Validation**: Use appropriate field types (email, tel, number)
6. **Layout**: Group related fields in rows
7. **Button placement**: Align submit with form content
8. **Mobile**: Stack columns on small screens
9. **Terms**: Include accept field for legal compliance
10. **Error messages**: Provide clear, helpful messages
